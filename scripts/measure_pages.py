"""Render every section as a standalone docx and measure real layout with Aspose.Words (evaluation mode).
Usage: DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1 LD_LIBRARY_PATH=/tmp/work/sslshim python3 measure_pages.py 3 [--no-charts]"""
import os, sys, importlib, tempfile
sys.path.insert(0, os.path.dirname(__file__))
from report_builder import new_document, render
import aspose.words as aw

CHARTS = "/tmp/work/charts"
parts = sys.argv[1].split(",")
pages = []
for n in parts:
    pages += importlib.import_module(f"content_part{n.strip()}").pages(CHARTS)
tmp = tempfile.mkdtemp()
flags = 0
for i, pg in enumerate(pages):
    doc = new_document()
    render(doc, pg, first=True)
    path = os.path.join(tmp, f"s{i}.docx")
    doc.save(path)
    d = aw.Document(path)
    # remove Aspose's evaluation watermark paragraph effect: it adds a paragraph at the start; measure bottom of last real line
    le = aw.layout.LayoutEnumerator(d)
    npages = d.page_count
    # find bottom of last line on last page (page_count may be inflated by the eval watermark text, see below)
    bottoms = {}
    le.move_first_child() if False else None
    # enumerate all lines
    def walk():
        while True:
            if le.type == aw.layout.LayoutEntityType.LINE:
                r = le.rectangle
                bottoms[le.page_index] = max(bottoms.get(le.page_index, 0), r.y + r.height)
            if le.type != aw.layout.LayoutEntityType.HEADER_FOOTER and le.move_first_child():
                walk()
                le.move_parent()
            if not le.move_next():
                break
    walk()
    last_pg = max(bottoms)
    fill = bottoms[last_pg] / 72.0  # inches from page top
    flag = ""
    if npages > 1: flag = f"  <-- SPILLS ({npages} pages; last page bottom {fill:.2f}in)"; flags += 1
    elif fill < 9.0: flag = "  <-- UNDERFILLED"; flags += 1
    print(f"{i+2:3d}  est {pg.height:5.2f}  real pages {npages}  bottom {fill:5.2f}in  {pg.title[:55]}{flag}")
print("flags", flags)
