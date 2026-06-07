import io
import re
import json
import time
import traceback
import contextlib
from pathlib import Path

from app.core.config import (
    VAULT_PATH,
    SANDBOX_TIMEOUT,
)


class SandboxManager:
    CODE_BLOCK_PATTERN = (
        r"```python\s*(.*?)```"
    )

    def __init__(
        self,
        vault_path=VAULT_PATH,
    ):
        self.vault_path = Path(
            vault_path
        )

        self.environments = {}

    # ====================================================
    # FILE HELPERS
    # ====================================================

    def topic_path(
        self,
        topic,
    ):
        return (
            self.vault_path
            / f"{topic}.md"
        )

    def load_topic(
        self,
        topic,
    ):
        path = self.topic_path(
            topic
        )

        if not path.exists():
            return None

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as f:
            return f.read()

    # ====================================================
    # CELL EXTRACTION
    # ====================================================

    def extract_cells(
        self,
        topic,
    ):
        content = self.load_topic(
            topic
        )

        if not content:
            return []

        matches = re.findall(
            self.CODE_BLOCK_PATTERN,
            content,
            re.DOTALL,
        )

        return [
            m.strip()
            for m in matches
        ]

    # ====================================================
    # ENVIRONMENT
    # ====================================================

    def create_environment(
        self,
        topic,
    ):
        self.environments[
            topic
        ] = {
            "__name__":
                "__sandbox__",
            "__topic__":
                topic,
        }

    def get_environment(
        self,
        topic,
    ):
        if (
            topic
            not in self.environments
        ):
            self.create_environment(
                topic
            )

        return self.environments[
            topic
        ]

    def reset_environment(
        self,
        topic,
    ):
        self.create_environment(
            topic
        )

    # ====================================================
    # EXECUTION
    # ====================================================

    def execute_code(
        self,
        code,
        env,
    ):
        output = io.StringIO()

        start_time = time.time()

        try:

            with contextlib.redirect_stdout(
                output
            ):
                exec(
                    code,
                    env,
                )

            runtime = (
                time.time()
                - start_time
            )

            if (
                runtime
                > SANDBOX_TIMEOUT
            ):
                return {
                    "success":
                        False,
                    "output":
                        (
                            "Execution "
                            "timeout."
                        ),
                    "runtime":
                        runtime,
                }

            return {
                "success":
                    True,
                "output":
                    output.getvalue(),
                "runtime":
                    runtime,
            }

        except Exception:

            return {
                "success":
                    False,
                "output":
                    traceback.format_exc(),
                "runtime":
                    (
                        time.time()
                        - start_time
                    ),
            }

    # ====================================================
    # SINGLE CELL
    # ====================================================

    def run_cell(
        self,
        topic,
        index,
        cumulative=True,
    ):
        cells = self.extract_cells(
            topic
        )

        if not cells:

            return {
                "success":
                    False,
                "output":
                    "No code cells found.",
            }

        if (
            index < 0
            or index >= len(cells)
        ):
            return {
                "success":
                    False,
                "output":
                    "Invalid cell index.",
            }

        if cumulative:

            env = self.get_environment(
                topic
            )

        else:

            env = {
                "__name__":
                    "__sandbox__"
            }

        result = self.execute_code(
            cells[index],
            env,
        )

        self.save_history(
            topic,
            index,
            result,
        )

        return result

    # ====================================================
    # RUN ALL
    # ====================================================

    def run_all(
        self,
        topic,
    ):
        self.reset_environment(
            topic
        )

        cells = self.extract_cells(
            topic
        )

        results = []

        for i in range(
            len(cells)
        ):

            result = self.run_cell(
                topic,
                i,
                cumulative=True,
            )

            results.append(
                result
            )

            if (
                not result[
                    "success"
                ]
            ):
                break

        return results

    # ====================================================
    # VARIABLE INSPECTION
    # ====================================================

    def get_variables(
        self,
        topic,
    ):
        env = self.get_environment(
            topic
        )

        variables = {}

        for k, v in env.items():

            if k.startswith(
                "__"
            ):
                continue

            try:
                variables[
                    k
                ] = repr(v)
            except Exception:
                variables[
                    k
                ] = (
                    "<unrepresentable>"
                )

        return variables

    # ====================================================
    # HISTORY
    # ====================================================

    def history_path(
        self,
        topic,
    ):
        return (
            self.vault_path
            / f"{topic}_history.json"
        )

    def load_history(
        self,
        topic,
    ):
        path = self.history_path(
            topic
        )

        if not path.exists():
            return []

        try:

            with open(
                path,
                "r",
                encoding="utf-8",
            ) as f:

                return json.load(
                    f
                )

        except Exception:

            return []

    def save_history(
        self,
        topic,
        cell_index,
        result,
    ):
        history = (
            self.load_history(
                topic
            )
        )

        history.append(
            {
                "timestamp":
                    time.time(),
                "cell":
                    cell_index,
                "success":
                    result[
                        "success"
                    ],
                "runtime":
                    result.get(
                        "runtime",
                        0,
                    ),
            }
        )

        with open(
            self.history_path(
                topic
            ),
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                history,
                f,
                indent=2,
            )

    # ====================================================
    # CELL PREVIEW
    # ====================================================

    def list_cells(
        self,
        topic,
    ):
        cells = self.extract_cells(
            topic
        )

        previews = []

        for i, cell in enumerate(
            cells
        ):
            preview = (
                cell[:200]
            )

            if (
                len(cell)
                > 200
            ):
                preview += "..."

            previews.append(
                {
                    "index":
                        i,
                    "preview":
                        preview,
                }
            )

        return previews


if __name__ == "__main__":

    sandbox = SandboxManager()

    print(
        sandbox.list_cells(
            "test"
        )
    )
