import re
import logfire


def parse_markdown(file_path: str) -> str:
    """
    Loads a Markdown file and returns the raw text with its heading structure
    and ``[[IMAGE: ...]]`` markers intact. The markers are kept here so the
    hierarchical chunker can attach the relevant screenshots to each chunk;
    the chunker strips them from the embedded text.
    """
    with logfire.span("📝 Markdown Parsing", filename=file_path):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except Exception as e:
            logfire.error(f"❌ Markdown Parse Failed: {e}")
            raise

        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()
