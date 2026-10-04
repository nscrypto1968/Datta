"""Render sections in groups of 4 (with real page breaks) and confirm each group lays out to exactly 4 pages."""
import os, sys, importlib, tempfile
sys.path.insert(0, os.path.dirname(__file__))
from report_builder import new_document, render
import aspose.words as aw
CHARTS = "/tmp/work/charts"
pages = []
for n in sys.argv[1].split(","):
    pages += importlib.import_module(f"content_part{n.strip()}").pages(CHARTS)
tmp = tempfile.mkdtemp(); bad = 0; G = 2
for g in range(0, len(pages), G):
    grp = pages[g:g+G]
    doc = new_document()
    for k, pg in enumerate(grp):
        render(doc, pg, first=(k == 0))
    path = os.path.join(tmp, f"g{g}.docx"); doc.save(path)
    d = aw.Document(path)
    n = d.page_count
    if "truncated" in d.get_text(): n = f"{n} (TRUNCATED)"
    ok = (n == len(grp))
    if not ok: bad += 1
    print(f"sections {g+2}-{g+1+len(grp)}: {len(grp)} expected, {n} rendered {'OK' if ok else '<-- CHECK'}  [{grp[0].title[:40]}]")
print("groups with mismatch:", bad)
