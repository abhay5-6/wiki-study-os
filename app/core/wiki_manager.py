import os
import re
import json
from pathlib import Path
from collections import defaultdict
from urllib.parse import quote

import networkx as nx
from pyvis.network import Network

from app.core.config import (
    VAULT_PATH,
    GRAPH_OUTPUT,
    LOCAL_GRAPH_OUTPUT,
)


class WikiManager:
    LINK_PATTERN = r"\[\[(.*?)\]\]"

    def __init__(self, vault_path=VAULT_PATH):
        self.vault_path = Path(vault_path)

    # ====================================================
    # PAGE MANAGEMENT
    # ====================================================

    def create_page(self, title):
        safe_title = re.sub(
            r'[\\/*?:"<>|]',
            "",
            title,
        ).strip()

        path = self.vault_path / f"{safe_title}.md"

        if path.exists():
            return safe_title

        content = (
            f"# {safe_title}\n\n"
            "#pending\n\n"
        )

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as f:
            f.write(content)

        return safe_title

    def delete_page(self, title):
        path = self.vault_path / f"{title}.md"

        if path.exists():
            path.unlink()

    def get_all_pages(self):
        pages = []

        for file in self.vault_path.glob("*.md"):
            pages.append(file.stem)

        pages.sort()

        return pages

    def read_page(self, title):
        path = self.vault_path / f"{title}.md"

        if not path.exists():
            return None

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as f:
            return f.read()

    def write_page(
        self,
        title,
        content,
    ):
        path = self.vault_path / f"{title}.md"

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as f:
            f.write(content)

    # ====================================================
    # STATUS
    # ====================================================

    def update_status(
        self,
        topic,
        status,
    ):
        allowed = {
            "read",
            "reading",
            "unread",
            "pending",
        }

        if status not in allowed:
            raise ValueError(
                f"Invalid status: {status}"
            )

        path = self.vault_path / f"{topic}.md"

        if not path.exists():
            return False

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as f:
            content = f.read()

        content = re.sub(
            r"#(read|reading|unread|pending)",
            "",
            content,
        )

        content = (
            f"#{status}\n\n"
            + content.strip()
        )

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as f:
            f.write(content)

        return True

    def get_status(self, topic):
        content = self.read_page(topic)

        if not content:
            return "unknown"

        match = re.search(
            r"#(read|reading|unread|pending)",
            content,
        )

        if match:
            return match.group(1)

        return "unknown"

    # ====================================================
    # LINK EXTRACTION
    # ====================================================

    def extract_links(
        self,
        content,
        topic=None,
        rich=False,
    ):
        links = []

        # Standard links: [[target]] or [[target|label]]
        # Use negative lookbehind to avoid matches starting with !
        matches = re.findall(
            r"(?<!\!)" + self.LINK_PATTERN,
            content,
        )

        for match in matches:
            if "|" in match:
                match = match.split("|")[0]
            page, sep, section = match.partition("#")
            page = page.strip()
            if not page and sep == "#" and topic:
                page = topic
            if page:
                if rich:
                    links.append({"target": page, "label": "", "type": "", "icon": ""})
                else:
                    links.append(page)

        # Rich links: @icon@ label/type [[target]]
        # We use a non-greedy match for icon but expect it to be followed by label/type
        rich_pattern = r"@(?P<icon>.*?)@\s+(?P<label>[^/\n]+)/(?P<type>[^\s\n]+)\s+\[\[(?P<target>[^\]\n]+)\]\]"
        for m in re.finditer(rich_pattern, content):
            target = m.group("target").strip()
            if "|" in target: target = target.split("|")[0]
            target = target.partition("#")[0].strip() or topic
            
            link_data = {
                "target": target,
                "label": m.group("label").strip(),
                "type": m.group("type").strip(),
                "icon": m.group("icon").strip()
            }
            if rich:
                links.append(link_data)
            else:
                links.append(target)

        return links

    def get_outgoing_links(
        self,
        topic,
        rich=False,
    ):
        content = self.read_page(topic)

        if not content:
            return []

        return self.extract_links(content, topic=topic, rich=rich)

    def get_backlinks(
        self,
        topic,
    ):
        backlinks = []

        for page in self.get_all_pages():

            if page == topic:
                continue

            links = self.get_outgoing_links(
                page
            )

            if topic in links:
                backlinks.append(page)

        return backlinks

    # ====================================================
    # AUTO LINKING
    # ====================================================

    def auto_link_page(self, topic):
        content = self.read_page(topic)

        if not content:
            return

        all_pages = set(
            self.get_all_pages()
        )

        all_pages.discard(topic)

        protected = re.split(r"(```.*?```|\[\[.*?\]\])", content, flags=re.DOTALL)
        for index in range(0, len(protected), 2):
            text = protected[index]
            for page in sorted(all_pages, key=len, reverse=True):
                text = re.sub(rf"(?<![\w\[])({re.escape(page)})(?![\w\]])", rf"[[\1]]", text, flags=re.IGNORECASE)
            protected[index] = text
        content = "".join(protected)

        self.write_page(
            topic,
            content,
        )

    def auto_link_all(self):
        pages = self.get_all_pages()

        for page in pages:
            self.auto_link_page(page)

    # ====================================================
    # GRAPH
    # ====================================================

    def build_graph(self):
        graph = nx.DiGraph()

        pages = set(self.get_all_pages())

        for page in pages:
            graph.add_node(page, ghost=False)

        for page in pages:

            links = (
                self.get_outgoing_links(
                    page,
                    rich=True
                )
            )

            for link in links:
                target = link["target"]
                if target not in graph:
                    graph.add_node(target, ghost=True)
                
                # Add edge with metadata if provided
                graph.add_edge(
                    page,
                    target,
                    label=link.get("label", ""),
                    type=link.get("type", ""),
                    icon=link.get("icon", "")
                )

        return graph

    def generate_graph(self, output_file=None, focus=None):
        if output_file is None:
            output_file = LOCAL_GRAPH_OUTPUT if focus else GRAPH_OUTPUT

        graph = self.build_graph()
        if focus and focus in graph:
            nodes = {focus, *graph.predecessors(focus), *graph.successors(focus)}
            graph = graph.subgraph(nodes).copy()

        net = Network(
            height="900px",
            width="100%",
            bgcolor="#0d1117",
            font_color="white",
            directed=True,
        )

        for node in graph.nodes():

            status = self.get_status(
                node
            )

            color = "#ff5555"

            if status == "read":
                color = "#50fa7b"

            elif status == "reading":
                color = "#f1fa8c"

            elif status == "pending":
                color = "#ff5555"

            net.add_node(
                node,
                label=node,
                color=color,
                url=f"wiki://note/{quote(node)}",
            )

        for src, dst in graph.edges():
            net.add_edge(
                src,
                dst,
            )

        output_file = Path(output_file)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        net.save_graph(str(output_file))
        graph_html = output_file.read_text(encoding="utf-8")
        navigation_script = """
<script>
network.on("doubleClick", function (params) {
    if (!params.nodes.length) return;
    const node = nodes.get(params.nodes[0]);
    if (node && node.url) window.location.href = node.url;
});
</script>
"""
        output_file.write_text(
            graph_html.replace("</body>", navigation_script + "</body>"),
            encoding="utf-8",
        )

        return str(output_file)

    # ====================================================
    # GLOSSARY
    # ====================================================

    def glossary_path(self):
        return (
            self.vault_path
            / "_glossary.json"
        )

    def load_glossary(self):
        path = self.glossary_path()

        if not path.exists():
            return {}

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as f:
            return json.load(f)

    def save_glossary(
        self,
        glossary,
    ):
        with open(
            self.glossary_path(),
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                glossary,
                f,
                indent=2,
                ensure_ascii=False,
            )

    def update_glossary(
        self,
        terms,
    ):
        glossary = (
            self.load_glossary()
        )

        glossary.update(terms)

        self.save_glossary(
            glossary
        )

    # ====================================================
    # SUGGEST LINKS
    # ====================================================

    def suggest_links(
        self,
        search_engine,
        threshold=0.65,
    ):
        suggestions = []

        pages = self.get_all_pages()

        if len(pages) < 2:
            return suggestions

        contents = []

        for page in pages:

            text = (
                self.read_page(page)
                or ""
            )

            contents.append(text)

        try:
            embeddings = search_engine.model.encode(contents, convert_to_numpy=True)
        except Exception:
            return suggestions

        norms = (
            embeddings
            / (
                (
                    embeddings ** 2
                ).sum(
                    axis=1,
                    keepdims=True,
                ) ** 0.5
                + 1e-10
            )
        )

        similarity = (
            norms @ norms.T
        )

        for i in range(
            len(pages)
        ):
            for j in range(
                i + 1,
                len(pages)
            ):

                score = float(
                    similarity[i][j]
                )

                if score >= threshold:

                    suggestions.append(
                        {
                            "from":
                                pages[i],
                            "to":
                                pages[j],
                            "similarity":
                                score,
                        }
                    )

        suggestions.sort(
            key=lambda x:
            x["similarity"],
            reverse=True,
        )

        return suggestions

    # ====================================================
    # STATISTICS
    # ====================================================

    def vault_stats(self):
        pages = self.get_all_pages()

        stats = {
            "total_pages":
                len(pages),
            "read": 0,
            "reading": 0,
            "pending": 0,
            "unread": 0,
        }

        for page in pages:

            status = (
                self.get_status(page)
            )

            if status in stats:
                stats[status] += 1

        return stats


if __name__ == "__main__":

    wiki = WikiManager()

    print(
        wiki.get_all_pages()
    )

    print(
        wiki.vault_stats()
    )
