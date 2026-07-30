from html.parser import HTMLParser
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "website"

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        key = "href" if tag in {"a", "link"} else "src" if tag in {"script", "iframe", "img"} else None
        if key and attrs.get(key):
            self.links.append(attrs[key])

errors = []
pages = list(SITE.glob("*.html"))
for page in pages:
    parser = Parser()
    parser.feed(page.read_text(encoding="utf-8"))
    for link in parser.links:
        if link.startswith(("http://","https://","mailto:","tel:","#")):
            continue
        target = (page.parent / link.split("#",1)[0].split("?",1)[0]).resolve()
        if not target.exists():
            errors.append(f"{page.name}: missing {link}")

meta = json.loads((SITE/"data"/"metadata.json").read_text(encoding="utf-8"))
rows = (SITE/"data"/"fema_declarations.csv").read_text(encoding="utf-8").splitlines()
if meta.get("record_count",0) < 1 or len(rows) < 2:
    errors.append("Published dashboard data is empty.")
if not (SITE/"downloads"/"plankind-capability-statement.pdf").exists():
    errors.append("Capability statement is missing.")
if not (SITE/"assets"/"og.png").exists():
    errors.append("Social preview image is missing.")
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"Validated {len(pages)} pages, all local links, {len(rows)-1} data rows, PDF, and social preview.")
