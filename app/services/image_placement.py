"""
Deterministic screenshot placement.

The manual's sections are written as numbered steps with ``[[IMAGE: ...]]``
markers sitting right after the step each screenshot illustrates. The LLM
paraphrases those steps, so after generation we match every marker's original
preceding step-text against the lines of the answer and re-insert the marker at
the best-matching line. No dependence on the model emitting anything.
"""
import re
from difflib import SequenceMatcher

_MARKER = re.compile(r"\[\[IMAGE:\s*([^\]]+?)\s*\]\]")
_WORD = re.compile(r"[a-z0-9]+")
_MATCH_THRESHOLD = 0.42


def _norm(text: str) -> str:
    return " ".join(_WORD.findall(text.lower()))


def _score(a: str, b: str) -> float:
    na, nb = _norm(a), _norm(b)
    if not na or not nb:
        return 0.0
    seq = SequenceMatcher(None, na, nb).ratio()
    wa, wb = set(na.split()), set(nb.split())
    jac = len(wa & wb) / len(wa | wb)
    return max(seq, jac)


def extract_marker_contexts(context_blocks: list[str]) -> list[tuple[str, str]]:
    """From the retrieved section text, return (image_name, preceding_step_text)
    pairs in document order. Consecutive markers share the same preceding step."""
    pairs: list[tuple[str, str]] = []
    seen: set[str] = set()

    for block in context_blocks:
        # Drop the "SOURCE:/SECTION:/CONTENT:" prefix and the breadcrumb line.
        body = block.split("CONTENT:", 1)[-1]
        lines = [ln.strip() for ln in body.splitlines()]
        last_text = ""
        for ln in lines:
            if not ln:
                continue
            names = _MARKER.findall(ln)
            if names:
                for name in names:
                    if name not in seen:
                        seen.add(name)
                        pairs.append((name, last_text))
                # a line that is only markers doesn't become context
                stripped = _MARKER.sub("", ln).strip()
                if stripped:
                    last_text = stripped
            else:
                last_text = ln
    return pairs


def place_images(answer: str, marker_contexts: list[tuple[str, str]]) -> str:
    """Insert [[IMAGE: name]] markers into the answer after the line that best
    matches each screenshot's original step. Unmatched screenshots are dropped."""
    answer = _MARKER.sub("", answer)  # ignore anything the model emitted itself
    if not marker_contexts:
        return answer.strip()

    lines = answer.split("\n")
    # line index -> list of image names to append after it
    inserts: dict[int, list[str]] = {}

    for name, ctx in marker_contexts:
        if not ctx:
            continue
        best_i, best_s = -1, 0.0
        for i, ln in enumerate(lines):
            if not ln.strip():
                continue
            s = _score(ctx, ln)
            if s > best_s:
                best_i, best_s = i, s
        if best_i >= 0 and best_s >= _MATCH_THRESHOLD:
            inserts.setdefault(best_i, []).append(name)

    if not inserts:
        return answer.strip()

    out: list[str] = []
    for i, ln in enumerate(lines):
        out.append(ln)
        for name in inserts.get(i, []):
            out.append(f"\n[[IMAGE: {name}]]\n")
    return "\n".join(out).strip()
