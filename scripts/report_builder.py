"""python-docx helpers: styles matching the original submission, block renderer and page-fill estimator."""
import math
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x12, 0x3A, 0x63)
TEAL = RGBColor(0x16, 0x7D, 0x9A)
BODY_PT = 10
TEXT_WIDTH_IN = 7.06
PAGE_HEIGHT_IN = 9.75          # usable height
WORDS_PER_LINE = 15.0
LINE_IN = 0.185                # 10pt * 1.12 line spacing ≈ 13.4pt
PARA_GAP_IN = 0.06
BULLET_GAP_IN = 0.03
ROW_IN = 0.20                  # single-line table row at 8.5pt incl. cell margins


def new_document():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Emu(7772400), Emu(10058400)
    sec.left_margin = sec.right_margin = Emu(658495)
    sec.top_margin, sec.bottom_margin = Emu(594360), Emu(548640)

    st = doc.styles["Normal"]
    st.font.name = "Aptos"; st.font.size = Pt(BODY_PT)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Aptos")
    st.paragraph_format.space_after = Pt(4); st.paragraph_format.space_before = Pt(0)
    st.paragraph_format.line_spacing = 1.12

    h1 = doc.styles["Heading 1"]
    h1.font.name = "Aptos Display"; h1.font.size = Pt(17); h1.font.bold = True; h1.font.color.rgb = NAVY
    h1.element.rPr.rFonts.set(qn("w:eastAsia"), "Aptos Display")
    h1.paragraph_format.space_before = Pt(0); h1.paragraph_format.space_after = Pt(8)

    h2 = doc.styles["Heading 2"]
    h2.font.name = "Aptos"; h2.font.size = Pt(11.5); h2.font.bold = True; h2.font.color.rgb = TEAL
    h2.paragraph_format.space_before = Pt(6); h2.paragraph_format.space_after = Pt(2)

    lb = doc.styles["List Bullet"]
    lb.font.size = Pt(BODY_PT); lb.paragraph_format.space_after = Pt(2); lb.paragraph_format.line_spacing = 1.1

    # footer page number
    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = footer.add_run("Fundamental Analysis of Fedbank Financial Services Limited  |  Page ")
    run.font.size = Pt(8); run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    _add_page_field(footer)
    return doc


def _add_page_field(paragraph):
    run = paragraph.add_run(); run.font.size = Pt(8)
    for tag, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if tag:
            el = OxmlElement("w:fldChar"); el.set(qn("w:fldCharType"), tag); run._r.append(el)
        else:
            el = OxmlElement("w:instrText"); el.set(qn("xml:space"), "preserve"); el.text = text; run._r.append(el)


def _shade(cell, hex_fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hex_fill)
    tcPr.append(shd)


def _cell_margins(table, top=30, bottom=30, left=70, right=70):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for side, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{side}"); el.set(qn("w:w"), str(val)); el.set(qn("w:type"), "dxa"); mar.append(el)
    tblPr.append(mar)


class Page:
    """Collects blocks for one page and estimates its printed height."""

    def __init__(self, title):
        self.title = title
        self.blocks = []
        self.height = 0.62  # break paragraph + heading

    def p(self, text, bold_lead=None, italic=False, size=None, align=None):
        self.blocks.append(("p", text, bold_lead, italic, size, align))
        words = len(text.split()) + (len(bold_lead.split()) if bold_lead else 0)
        self.height += math.ceil(words / WORDS_PER_LINE) * LINE_IN + PARA_GAP_IN
        return self

    def h2(self, text):
        self.blocks.append(("h2", text))
        self.height += 0.30
        return self

    def bullets(self, items, size=None):
        self.blocks.append(("bul", items, size))
        for it in items:
            self.height += math.ceil(len(it.split()) / (WORDS_PER_LINE - 1.5)) * LINE_IN + BULLET_GAP_IN
        self.height += 0.05
        return self

    def table(self, headers, rows, widths=None, source=None, font=8.5, align_num=True, first_col_bold=False):
        self.blocks.append(("tbl", headers, rows, widths, source, font, align_num, first_col_bold))
        total_w = sum(widths) if widths else TEXT_WIDTH_IN
        # estimate wrapped lines per row
        char_w = font * 0.0070            # average Aptos glyph width in inches at this size
        row_in = (font * 1.2 + 3.5) / 72   # one text line + cell margins
        def row_lines(cells):
            lines = 1
            for i, c in enumerate(cells):
                w = (widths[i] if widths else total_w / len(cells)) - 0.1
                chars_per_line = max(6, int(w / char_w))
                txt = str(c)
                n = sum(math.ceil(max(1, len(part)) / chars_per_line) for part in txt.split("\n"))
                lines = max(lines, n)
            return lines
        self.height += row_in * row_lines(headers) * 1.05
        for r in rows:
            self.height += row_in * row_lines(r)
        self.height += 0.12 + (0.2 if source else 0)
        return self

    def fig(self, path, caption, height_in=2.5, width=6.4):
        """height_in is the rendered height at 6.4in width; scaled if a narrower width is given."""
        h = height_in * width / 6.4
        self.blocks.append(("fig", path, caption, h, width))
        self.height += h + 0.30
        return self

    def kpis(self, items, cols=4):
        """items: list of (value, label)."""
        self.blocks.append(("kpi", items, cols))
        self.height += 0.62 * math.ceil(len(items) / cols) + 0.1
        return self

    def space(self, inches=0.15):
        self.blocks.append(("sp", inches)); self.height += inches
        return self


def render(doc, page, first=False):
    h = doc.add_heading(page.title, level=1)
    if not first:
        h.paragraph_format.page_break_before = True
    for b in page.blocks:
        kind = b[0]
        if kind == "p":
            _, text, lead, italic, size, align = b
            para = doc.add_paragraph()
            if lead:
                r = para.add_run(lead + " "); r.bold = True
            r = para.add_run(text); r.italic = italic
            if size: r.font.size = Pt(size)
            if align == "center": para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            elif align == "justify" or align is None: para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        elif kind == "h2":
            doc.add_heading(b[1], level=2)
        elif kind == "bul":
            bsize = b[2] if len(b) > 2 else None
            for it in b[1]:
                para = doc.add_paragraph(style="List Bullet")
                if "::" in it:
                    lead, rest = it.split("::", 1)
                    r = para.add_run(lead.strip() + ": "); r.bold = True; r2 = para.add_run(rest.strip())
                    runs = [r, r2]
                else:
                    runs = [para.add_run(it)]
                if bsize:
                    for r in runs: r.font.size = Pt(bsize)
                    para.paragraph_format.space_after = Pt(2)
        elif kind == "tbl":
            _, headers, rows, widths, source, font, align_num, fcb = b
            t = doc.add_table(rows=1 + len(rows), cols=len(headers))
            t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
            _cell_margins(t)
            for i, h in enumerate(headers):
                c = t.rows[0].cells[i]; c.text = ""
                r = c.paragraphs[0].add_run(str(h)); r.bold = True; r.font.size = Pt(font); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                _shade(c, "123A63")
                c.paragraphs[0].paragraph_format.space_after = Pt(0)
            for ri, row in enumerate(rows):
                for ci, val in enumerate(row):
                    c = t.rows[ri + 1].cells[ci]; c.text = ""
                    pr = c.paragraphs[0]; pr.paragraph_format.space_after = Pt(0)
                    r = pr.add_run(str(val)); r.font.size = Pt(font)
                    if fcb and ci == 0: r.bold = True
                    if align_num and ci > 0 and _looks_numeric(str(val)):
                        pr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                    if ri % 2 == 1: _shade(c, "F2F6FA")
            if widths:
                for row in t.rows:
                    for ci, w in enumerate(widths):
                        row.cells[ci].width = Inches(w)
            if source:
                sp = doc.add_paragraph(); r = sp.add_run("Source: " + source); r.italic = True; r.font.size = Pt(7.5)
                r.font.color.rgb = RGBColor(0x55, 0x55, 0x55); sp.paragraph_format.space_after = Pt(4); sp.paragraph_format.space_before = Pt(2)
            else:
                doc.add_paragraph().paragraph_format.space_after = Pt(2)
        elif kind == "fig":
            _, path, caption, h, w = b
            para = doc.add_paragraph(); para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_after = Pt(0)
            para.add_run().add_picture(path, width=Inches(w))
            cp = doc.add_paragraph(); cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = cp.add_run(caption); r.italic = True; r.font.size = Pt(7.5); r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
            cp.paragraph_format.space_after = Pt(4)
        elif kind == "kpi":
            _, items, cols = b
            n = len(items); nrows = math.ceil(n / cols)
            t = doc.add_table(rows=nrows, cols=cols); t.alignment = WD_TABLE_ALIGNMENT.CENTER
            _cell_margins(t, 40, 40, 60, 60)
            for i, (val, lab) in enumerate(items):
                c = t.rows[i // cols].cells[i % cols]; c.text = ""
                _shade(c, "EEF3F8")
                p1 = c.paragraphs[0]; p1.alignment = WD_ALIGN_PARAGRAPH.CENTER; p1.paragraph_format.space_after = Pt(0)
                r = p1.add_run(str(val)); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = NAVY
                p2 = c.add_paragraph(); p2.alignment = WD_ALIGN_PARAGRAPH.CENTER; p2.paragraph_format.space_after = Pt(0)
                r = p2.add_run(lab); r.font.size = Pt(7.5); r.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
            doc.add_paragraph().paragraph_format.space_after = Pt(2)
        elif kind == "sp":
            para = doc.add_paragraph(); para.paragraph_format.space_after = Pt(b[1] * 72)


def _looks_numeric(s):
    s = s.replace(",", "").replace("₹", "").replace("%", "").replace("(", "-").replace(")", "").replace("x", "").strip()
    try:
        float(s); return True
    except ValueError:
        return s in ("-", "–", "n.a.", "NA", "Nil")
