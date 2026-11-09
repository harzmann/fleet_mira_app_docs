"""Check generated HTML links, assets and local anchors without external network calls."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parents[1] / "site"
prefix = "/fleet_mira_app_docs/"


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag in {"a", "link"} and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag in {"img", "script"} and attrs.get("src"):
            self.links.append(attrs["src"])


pages = {p.resolve(): Page(p.read_text(encoding="utf-8")) for p in root.rglob("*.html")}
assert (root / "index.html").resolve() in pages
assert (root / "de/index.html").resolve() in pages
checked = 0
for path, page in pages.items():
    for value in page.links:
        url = urlsplit(value)
        if url.scheme or url.netloc:
            continue
        target_path = unquote(url.path)
        if target_path.startswith(prefix):
            target = root / target_path[len(prefix):]
        elif target_path.startswith("/"):
            target = root / target_path.lstrip("/")
        else:
            target = path.parent / target_path if target_path else path
        if target.is_dir():
            target = target / "index.html"
        target = target.resolve()
        assert target.is_file(), f"Broken generated link in {path}: {value}"
        if url.fragment and target in pages:
            assert unquote(url.fragment) in pages[target].ids, f"Missing anchor in {path}: {value}"
        checked += 1
print(f"Validated {len(pages)} HTML pages and {checked} local links/assets/anchors")
