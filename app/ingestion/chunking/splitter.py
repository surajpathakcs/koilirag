import re
from typing import List, Dict
import logfire

DOC_TITLE = "Koili TMS Manual"
MAX_CHUNK_CHARS = 2400

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
# Leading section number such as "12.3.1", "10.10" or "6.3.2." followed by a title.
_NUM_RE = re.compile(r"^(\d+(?:\.\d+)*)\.?\s+(.*)$")
# Screenshot markers like "[[IMAGE: manual_img_042.jpg]]".
_IMAGE_MARKER = re.compile(r"\[\[IMAGE:\s*([^\]]+?)\s*\]\]")


def _extract_images(text: str) -> tuple[str, List[str]]:
    """Pull image filenames out of a block and return (clean_text, filenames)."""
    images = [m.group(1) for m in _IMAGE_MARKER.finditer(text)]
    clean = _IMAGE_MARKER.sub("", text)
    clean = re.sub(r"[ \t]+\n", "\n", clean)
    clean = re.sub(r"\n{3,}", "\n\n", clean).strip()
    return clean, images


def _parse_sections(text: str) -> List[Dict]:
    """
    Walk the Markdown line by line and cut it into sections at every heading.
    Level is taken from the section number when present (``12.3.1`` -> level 3),
    otherwise from the number of ``#`` characters. Each section owns only the
    body text between its heading and the next heading of any level.
    """
    sections: List[Dict] = []
    cur: Dict | None = None

    for line in text.split("\n"):
        m = _HEADING_RE.match(line)
        if m:
            heading_text = m.group(2).strip()
            num_m = _NUM_RE.match(heading_text)
            if num_m:
                number = num_m.group(1)
                title = num_m.group(2).strip() or number
                level = number.count(".") + 1
            else:
                number = None
                title = heading_text
                level = len(m.group(1))

            if cur is not None:
                sections.append(cur)
            cur = {"level": level, "number": number, "title": title, "body": []}
        else:
            if cur is None:
                cur = {"level": 0, "number": None, "title": DOC_TITLE, "body": []}
            cur["body"].append(line)

    if cur is not None:
        sections.append(cur)
    return sections


def _label(section: Dict) -> str:
    if section["number"]:
        return f"{section['number']}. {section['title']}"
    return section["title"]


def _split_oversized_body(body: str) -> List[str]:
    """Split a long section body on paragraph boundaries, never mid-paragraph."""
    if len(body) <= MAX_CHUNK_CHARS:
        return [body]

    parts: List[str] = []
    current = ""
    for para in body.split("\n\n"):
        if current and len(current) + len(para) + 2 > MAX_CHUNK_CHARS:
            parts.append(current.strip())
            current = para + "\n\n"
        else:
            current += para + "\n\n"
    if current.strip():
        parts.append(current.strip())
    return parts


def chunk_markdown_hierarchical(text: str) -> List[Dict]:
    """
    Hierarchy-aware chunker. Produces one chunk per leaf section so that each
    chunk is a single self-contained context. The full heading breadcrumb
    (``Koili TMS Manual > 6. Branch > 6.3. View Branch Details > ...``) is
    prepended to every chunk so it stands alone for embedding and retrieval.

    ``[[IMAGE: ...]]`` markers are stripped from the embedded text but their
    filenames are kept per chunk (in order) so screenshots can be shown later.

    Returns a list of dicts: ``text``, ``section_number``, ``title``,
    ``section_path``, ``part`` and ``images``.
    """
    with logfire.span("✂️ Hierarchical Markdown Chunking", text_length=len(text)):
        sections = _parse_sections(text)

        # Running stack of ancestor sections, kept in level order.
        stack: List[Dict] = []
        chunks: List[Dict] = []

        for section in sections:
            level = section["level"]
            while stack and stack[-1]["level"] >= level:
                stack.pop()

            crumb = [DOC_TITLE] + [_label(s) for s in stack if s["level"] > 0]
            crumb.append(_label(section))
            section_path = " > ".join(crumb)

            stack.append(section)

            body = "\n".join(section["body"]).strip()
            if not body:
                # Heading with no prose of its own (pure parent) — skip.
                continue

            parts = _split_oversized_body(body)
            total = len(parts)
            for idx, part in enumerate(parts, start=1):
                clean_part, images = _extract_images(part)
                if not clean_part:
                    # Part held only screenshots — fold them into the previous chunk.
                    if chunks and images:
                        chunks[-1]["images"].extend(images)
                    continue
                suffix = f" (part {idx} of {total})" if total > 1 else ""
                chunk_text_value = f"{section_path}{suffix}\n\n{clean_part}"
                chunks.append(
                    {
                        "text": chunk_text_value,
                        "section_number": section["number"] or "",
                        "title": section["title"],
                        "section_path": section_path,
                        "part": idx,
                        "images": images,
                    }
                )

        logfire.info(f"✅ Generated {len(chunks)} hierarchical chunks")
        return chunks


def chunk_text(text: str, chunk_size: int = 1500) -> List[str]:
    """
    Simple semantic-ish chunker that splits by paragraphs.
    Ensures chunks do not exceed the specified size.
    """
    with logfire.span("✂️ Text Chunking", text_length=len(text)):
        if not text.strip(): 
            return []
            
        paragraphs = text.split("\n\n")
        chunks = []
        current_chunk = ""
        
        for p in paragraphs:
            if len(current_chunk) + len(p) < chunk_size:
                current_chunk += p + "\n\n"
            else:
                if current_chunk.strip():
                    chunks.append(current_chunk.strip())
                current_chunk = p + "\n\n"
        
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
            
        valid_chunks = [c for c in chunks if c.strip()]
        logfire.info(f"✅ Generated {len(valid_chunks)} chunks")
        return valid_chunks
