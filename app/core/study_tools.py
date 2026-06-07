import re
import random
from pathlib import Path

from app.core.config import (
    VAULT_PATH,
    DEFAULT_MODEL,
)


class StudyTools:
    def __init__(self, vault_path=VAULT_PATH):
        self.vault_path = Path(vault_path)

    # ====================================================
    # FILE HELPERS
    # ====================================================

    def load_topic(self, topic):
        path = self.vault_path / f"{topic}.md"

        if not path.exists():
            return None

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as f:
            return f.read()

    def clean_text(self, text):
        text = re.sub(
            r"\[\[(.*?)\]\]",
            r"\1",
            text,
        )

        text = re.sub(
            r"!\[\[(.*?)\]\]",
            "",
            text,
        )

        text = re.sub(
            r"#+",
            "",
            text,
        )

        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        return text.strip()

    # ====================================================
    # KEY TERMS
    # ====================================================

    def extract_key_terms(
        self,
        topic,
        top_n=20,
    ):
        content = self.load_topic(
            topic
        )

        if not content:
            return []

        content = self.clean_text(
            content
        )

        words = re.findall(
            r"\b[A-Z][A-Za-z0-9_-]+\b",
            content,
        )

        freq = {}

        for word in words:
            freq[word] = (
                freq.get(word, 0)
                + 1
            )

        terms = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return terms[:top_n]

    # ====================================================
    # SUMMARY
    # ====================================================

    def generate_summary(
        self,
        topic,
        max_sentences=10,
    ):
        content = self.load_topic(
            topic
        )

        if not content:
            return "Topic not found."

        text = self.clean_text(
            content
        )

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text,
        )

        if len(sentences) <= max_sentences:
            return "\n".join(sentences)

        scored = []

        keywords = {}

        words = re.findall(
            r"\w+",
            text.lower(),
        )

        for w in words:
            if len(w) > 4:
                keywords[w] = (
                    keywords.get(w, 0)
                    + 1
                )

        for sentence in sentences:

            score = 0

            sentence_words = re.findall(
                r"\w+",
                sentence.lower(),
            )

            for w in sentence_words:
                score += keywords.get(
                    w,
                    0,
                )

            scored.append(
                (
                    score,
                    sentence,
                )
            )

        scored.sort(
            reverse=True
        )

        selected = [
            x[1]
            for x in scored[
                :max_sentences
            ]
        ]

        return "\n".join(
            selected
        )

    # ====================================================
    # FLASHCARDS
    # ====================================================

    def generate_flashcards(
        self,
        topic,
    ):
        content = self.load_topic(
            topic
        )

        if not content:
            return "Topic not found."

        terms = (
            self.extract_key_terms(
                topic,
                15,
            )
        )

        cards = []

        for term, _ in terms:

            pattern = (
                rf"{re.escape(term)}.*?[.!?]"
            )

            match = re.search(
                pattern,
                content,
                re.DOTALL,
            )

            definition = (
                match.group(0)
                if match
                else "Definition not found."
            )

            cards.append(
                {
                    "front": term,
                    "back": definition,
                }
            )

        output = []

        for i, card in enumerate(
            cards,
            start=1,
        ):
            output.append(
                f"\nCARD {i}"
            )
            output.append(
                f"Q: {card['front']}"
            )
            output.append(
                f"A: {card['back']}"
            )

        return "\n".join(
            output
        )

    # ====================================================
    # QUIZ
    # ====================================================

    def generate_quiz(
        self,
        topic,
        n=5,
    ):
        content = self.load_topic(
            topic
        )

        if not content:
            return "Topic not found."

        sentences = re.split(
            r"(?<=[.!?])\s+",
            self.clean_text(
                content
            ),
        )

        questions = []

        for sentence in sentences:

            caps = re.findall(
                r"\b[A-Z][A-Za-z0-9_-]+\b",
                sentence,
            )

            if not caps:
                continue

            keyword = caps[0]

            question = (
                sentence.replace(
                    keyword,
                    "_____",
                    1,
                )
            )

            questions.append(
                (
                    question,
                    keyword,
                )
            )

        random.shuffle(
            questions
        )

        questions = questions[:n]

        output = []

        for i, (
            q,
            ans,
        ) in enumerate(
            questions,
            start=1,
        ):
            output.append(
                f"\nQ{i}. {q}"
            )
            output.append(
                f"Answer: {ans}"
            )

        return "\n".join(
            output
        )

    # ====================================================
    # LLM SUMMARY
    # ====================================================

    def _completion(self, messages):
        from litellm import completion
        kwargs = {"api_base": "http://localhost:11434"} if DEFAULT_MODEL.startswith("ollama/") else {}
        return completion(model=DEFAULT_MODEL, messages=messages, **kwargs)

    def llm_summary(
        self,
        topic,
    ):
        content = self.load_topic(
            topic
        )

        if not content:
            return "Topic not found."

        try:

            response = self._completion(
                [
                    {
                        "role": "user",
                        "content":
                        f"""
Summarize the following study material.

Provide:

1. Executive Summary
2. Key Concepts
3. Important Formulas
4. Exam Tips

CONTENT:

{content[:12000]}
""",
                    }
                ],
            )

            return (
                response
                .choices[0]
                .message.content
            )

        except Exception as e:

            return (
                "LLM summary failed:\n"
                f"{e}"
            )

    # ====================================================
    # LLM FLASHCARDS
    # ====================================================

    def llm_flashcards(
        self,
        topic,
        count=20,
    ):
        content = self.load_topic(
            topic
        )

        if not content:
            return "Topic not found."

        try:

            response = self._completion(
                [
                    {
                        "role": "user",
                        "content":
                        f"""
Create {count} study flashcards.

Format:

Q:
A:

Material:

{content[:12000]}
""",
                    }
                ],
            )

            return (
                response
                .choices[0]
                .message.content
            )

        except Exception as e:

            return (
                "Flashcard generation failed:\n"
                f"{e}"
            )

    # ====================================================
    # LLM QUIZ
    # ====================================================

    def llm_quiz(
        self,
        topic,
        count=10,
    ):
        content = self.load_topic(
            topic
        )

        if not content:
            return "Topic not found."

        try:

            response = self._completion(
                [
                    {
                        "role": "user",
                        "content":
                        f"""
Generate a quiz.

Requirements:

- {count} questions
- Mix conceptual
- Numerical if possible
- Include answers

Material:

{content[:12000]}
""",
                    }
                ],
            )

            return (
                response
                .choices[0]
                .message.content
            )

        except Exception as e:

            return (
                "Quiz generation failed:\n"
                f"{e}"
            )

    # ====================================================
    # STUDY REPORT
    # ====================================================

    def study_report(
        self,
        topic,
    ):
        terms = self.extract_key_terms(
            topic
        )

        summary = (
            self.generate_summary(
                topic,
                5,
            )
        )

        report = []

        report.append(
            f"TOPIC: {topic}"
        )

        report.append(
            "\n=== SUMMARY ===\n"
        )

        report.append(
            summary
        )

        report.append(
            "\n=== KEY TERMS ===\n"
        )

        for term, count in terms:
            report.append(
                f"{term}: {count}"
            )

        return "\n".join(
            report
        )


if __name__ == "__main__":

    study = StudyTools()

    print(
        study.study_report(
            "test"
        )
    )
