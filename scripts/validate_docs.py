"""Check paired public documentation sources and local Markdown destinations."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import re

root = Path(__file__).resolve().parents[1]
docs = root / "docs"
english = {p.relative_to(docs / "en") for p in (docs / "en").rglob("*.md")}
german = {p.relative_to(docs / "de") for p in (docs / "de").rglob("*.md")}
assert english == german and len(english) >= 17, "English/German pages must be paired"
for image in (docs / "assets/screenshots").rglob("*.png"):
    translated = docs / "de/assets/screenshots" / image.relative_to(docs / "assets/screenshots")
    assert translated.is_file() and hashlib.sha256(image.read_bytes()).digest() == hashlib.sha256(translated.read_bytes()).digest(), "Run python scripts/sync_assets.py after changing shared screenshots"
checked = 0
for page in [*(docs / "en").rglob("*.md"), *(docs / "de").rglob("*.md")]:
    text = page.read_text(encoding="utf-8")
    assert text.startswith("# "), f"Missing page heading: {page}"
    assert not re.search(r"\b(?:TODO|FIXME|PLACEHOLDER)\b", text), page
    assert not re.search(r"ghp_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{25,}|-----BEGIN .*PRIVATE KEY-----", text), page
    for destination in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text):
        url = urlsplit(destination)
        if url.scheme or url.netloc or not url.path:
            continue
        path = unquote(url.path)
        candidates = [page.parent / path]
        if path.startswith("assets/"):
            candidates.append(docs / path)
        assert any(p.is_file() for p in candidates), f"Broken destination in {page}: {destination}"
        checked += 1
print(f"Validated {len(english)} language pairs and {checked} local Markdown destinations")
