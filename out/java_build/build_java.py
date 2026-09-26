#!/usr/bin/env python3
"""Build the Java Source Code Analysis report (body PDF).

Content lives in content/jcN.py files, each defining BLOCKS - a list of tuples:
    ("part", title, intro)                       - part opener (TOC level 0)
    ("h2", title)                                - section heading (TOC level 1)
    ("h3", title)                                - sub-heading
    ("body", text)                               - paragraph
    ("bullets", [items])                         - bullet list
    ("numbers", [items])                         - numbered list
    ("table", {caption, headers, rows, widths})  - data table
    ("code", text)                               - monospace block
    ("callout", label, text)                     - accent callout box
    ("quote", text)                              - pull quote

Inline markup (auto-escaped first): **bold**  *italic*  `mono`  ^{sup}  _{sub}
"""
import os
import re
import sys
import hashlib

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, CondPageBreak, HRFlowable, XPreformatted,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

BUILD = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BUILD, "content")
OUT_PDF = os.path.join(BUILD, "body.pdf")

DOC_TITLE = "Java Source Code Analysis - Tips, Tricks and Concepts"

# ---------------------------------------------------------------- fonts
FDIR = "/usr/share/fonts/truetype"
pdfmetrics.registerFont(TTFont("LibSerif", FDIR + "/liberation/LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LibSerif-Bold", FDIR + "/liberation/LiberationSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("LibSerif-Italic", FDIR + "/liberation/LiberationSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("LibSerif-BoldItalic", FDIR + "/liberation/LiberationSerif-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("LibSans", FDIR + "/liberation/LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LibSans-Bold", FDIR + "/liberation/LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Mono", FDIR + "/dejavu/DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont("Mono-Bold", FDIR + "/dejavu/DejaVuSansMono-Bold.ttf"))
registerFontFamily("LibSerif", normal="LibSerif", bold="LibSerif-Bold",
                   italic="LibSerif-Italic", boldItalic="LibSerif-BoldItalic")
registerFontFamily("LibSans", normal="LibSans", bold="LibSans-Bold",
                   italic="LibSans", boldItalic="LibSans-Bold")
registerFontFamily("Mono", normal="Mono", bold="Mono-Bold",
                   italic="Mono", boldItalic="Mono-Bold")

# ------------------------------------------------- palette (pdf.py palette.cascade)
PAGE_BG       = colors.HexColor('#f1f0ef')
SECTION_BG    = colors.HexColor('#f1f0f0')
CARD_BG       = colors.HexColor('#e9e8e6')
TABLE_STRIPE  = colors.HexColor('#f1f0ed')
HEADER_FILL   = colors.HexColor('#675c3c')
COVER_BLOCK   = colors.HexColor('#625a41')
BORDER        = colors.HexColor('#d6d1c3')
ICON          = colors.HexColor('#9f8a4b')
ACCENT        = colors.HexColor('#2689aa')
ACCENT_2      = colors.HexColor('#43c843')
TEXT_PRIMARY  = colors.HexColor('#1c1b19')
TEXT_MUTED    = colors.HexColor('#87847d')

TABLE_HEADER_COLOR = ACCENT
TABLE_HEADER_TEXT = colors.white
TABLE_ROW_EVEN = colors.white
TABLE_ROW_ODD = TABLE_STRIPE

# ---------------------------------------------------------------- geometry
PAGE_W, PAGE_H = A4
LM = RM = 0.9 * inch
TM = 0.95 * inch
BM = 0.85 * inch
AVAIL_W = PAGE_W - LM - RM
AVAIL_H = PAGE_H - TM - BM
MAX_KEEP_HEIGHT = PAGE_H * 0.4
H1_ORPHAN = AVAIL_H * 0.30
H2_ORPHAN = AVAIL_H * 0.15

# ---------------------------------------------------------------- styles
S = {}
S["part_title"] = ParagraphStyle("PartTitle", fontName="LibSans-Bold", fontSize=19,
                                 leading=24, textColor=TEXT_PRIMARY, spaceBefore=0, spaceAfter=4)
S["part_kicker"] = ParagraphStyle("PartKicker", fontName="LibSans", fontSize=9,
                                  leading=12, textColor=ACCENT, spaceBefore=0, spaceAfter=6)
S["part_intro"] = ParagraphStyle("PartIntro", fontName="LibSerif-Italic", fontSize=10.5,
                                 leading=15.5, textColor=TEXT_MUTED, alignment=TA_LEFT,
                                 spaceBefore=6, spaceAfter=14)
S["h2"] = ParagraphStyle("H2", fontName="LibSans-Bold", fontSize=13.5, leading=17.5,
                         textColor=ACCENT, spaceBefore=16, spaceAfter=6)
S["h3"] = ParagraphStyle("H3", fontName="LibSans-Bold", fontSize=11, leading=14.5,
                         textColor=TEXT_PRIMARY, spaceBefore=11, spaceAfter=4)
S["body"] = ParagraphStyle("Body", fontName="LibSerif", fontSize=10.3, leading=15.2,
                           textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY, spaceBefore=0, spaceAfter=8)
S["bullet"] = ParagraphStyle("Bullet", fontName="LibSerif", fontSize=10.3, leading=14.6,
                             textColor=TEXT_PRIMARY, alignment=TA_LEFT,
                             leftIndent=16, bulletIndent=4, spaceBefore=0, spaceAfter=3.5)
S["numbered"] = ParagraphStyle("Numbered", parent=S["bullet"], leftIndent=20, bulletIndent=4)
S["cell_head"] = ParagraphStyle("CellHead", fontName="LibSans-Bold", fontSize=9.2, leading=12,
                                textColor=TABLE_HEADER_TEXT, alignment=TA_LEFT)
S["cell"] = ParagraphStyle("Cell", fontName="LibSerif", fontSize=9.4, leading=12.8,
                           textColor=TEXT_PRIMARY, alignment=TA_LEFT)
S["caption"] = ParagraphStyle("Caption", fontName="LibSerif-Italic", fontSize=8.6, leading=11.5,
                              textColor=TEXT_MUTED, alignment=TA_CENTER, spaceBefore=0, spaceAfter=0)
S["code"] = ParagraphStyle("Code", fontName="Mono", fontSize=8.2, leading=11.4,
                           textColor=TEXT_PRIMARY, alignment=TA_LEFT)
S["callout"] = ParagraphStyle("Callout", fontName="LibSerif", fontSize=9.8, leading=14,
                              textColor=TEXT_PRIMARY, alignment=TA_LEFT)
S["quote"] = ParagraphStyle("Quote", fontName="LibSerif-Italic", fontSize=10.3, leading=15,
                            textColor=TEXT_MUTED, leftIndent=10, alignment=TA_LEFT)
S["toc_title"] = ParagraphStyle("TocTitle", fontName="LibSans-Bold", fontSize=17, leading=22,
                                textColor=TEXT_PRIMARY, spaceAfter=14)

# ---------------------------------------------------------------- inline markup
from xml.sax.saxutils import escape as _xml_escape

def esc(t):
    return _xml_escape(t)

def inline(t):
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    t = re.sub(r"\^\{([^}]+)\}", r"<super>\1</super>", t)
    t = re.sub(r"_\{([^}]+)\}", r"<sub>\1</sub>", t)
    t = re.sub(r"`([^`\n]+)`", r'<font face="Mono" size="8.6">\1</font>', t)
    return t

def safe_keep_together(elements):
    total_h = 0
    for el in elements:
        try:
            _w, h = el.wrap(AVAIL_W, AVAIL_H)
        except Exception:
            h = 0
        total_h += h
    if total_h <= MAX_KEEP_HEIGHT:
        return [KeepTogether(elements)]
    elif len(elements) >= 2:
        return [KeepTogether(elements[:2])] + list(elements[2:])
    return list(elements)

# ---------------------------------------------------------------- block renderers
def r_part(title, intro):
    key = "part_" + hashlib.md5(title.encode()).hexdigest()[:8]
    p = Paragraph('<a name="%s"/>%s' % (key, esc(title)), S["part_title"])
    p.bookmark_name = title
    p.bookmark_level = 0
    p.bookmark_text = title
    p.bookmark_key = key
    kicker_text = "ANALYSIS REPORT" if not title.startswith("Section ") else "SECTION"
    kicker = Paragraph(esc(kicker_text), S["part_kicker"])
    rule = HRFlowable(width="100%", thickness=1.6, color=ACCENT, spaceBefore=2, spaceAfter=2)
    intro_p = Paragraph(inline(intro), S["part_intro"])
    return [Spacer(1, 10), CondPageBreak(H1_ORPHAN), kicker, p, rule, intro_p, Spacer(1, 4)]

def r_h2(title, counter):
    key = "h2_" + hashlib.md5((title + str(counter)).encode()).hexdigest()[:8]
    p = Paragraph('<a name="%s"/>%s' % (key, esc(title)), S["h2"])
    p.bookmark_name = title
    p.bookmark_level = 1
    p.bookmark_text = title
    p.bookmark_key = key
    return [CondPageBreak(H2_ORPHAN), p]

def r_h3(title):
    return [CondPageBreak(55), Paragraph(esc(title), S["h3"])]

def r_body(text):
    return [Paragraph(inline(text), S["body"])]

def r_bullets(items):
    out = []
    for it in items:
        out.append(Paragraph(inline(it), S["bullet"], bulletText="•"))
    out.append(Spacer(1, 4))
    return out

def r_numbers(items):
    out = []
    for i, it in enumerate(items, 1):
        out.append(Paragraph(inline(it), S["numbered"], bulletText="%d." % i))
    out.append(Spacer(1, 4))
    return out

def r_table(spec):
    headers = spec["headers"]
    rows = spec["rows"]
    widths = spec.get("widths")
    ncols = len(headers)
    if not widths:
        widths = [1.0 / ncols] * ncols
    total = sum(widths)
    col_widths = [w / total * AVAIL_W for w in widths]
    data = [[Paragraph("<b>%s</b>" % inline(h), S["cell_head"]) for h in headers]]
    for row in rows:
        data.append([Paragraph(inline(str(c)), S["cell"]) for c in row])
    t = Table(data, colWidths=col_widths, hAlign="CENTER", repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_COLOR),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(data)):
        style.append(("BACKGROUND", (0, i), (-1, i),
                      TABLE_ROW_ODD if i % 2 == 0 else TABLE_ROW_EVEN))
    t.setStyle(TableStyle(style))
    out = [Spacer(1, 8), t]
    cap = spec.get("caption")
    if cap:
        out += [Spacer(1, 4), Paragraph(inline(cap), S["caption"])]
    out.append(Spacer(1, 10))
    return out

def r_code(text):
    pre = XPreformatted(esc(text.rstrip("\n")), S["code"])
    t = Table([[pre]], colWidths=[AVAIL_W * 0.96], hAlign="CENTER")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SECTION_BG),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return [Spacer(1, 6)] + safe_keep_together([t]) + [Spacer(1, 8)]

def r_callout(label, text):
    para = Paragraph("<b>%s.</b>  %s" % (inline(label), inline(text)), S["callout"])
    t = Table([[para]], colWidths=[AVAIL_W * 0.97], hAlign="CENTER")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("LINEBEFORE", (0, 0), (0, -1), 3, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return [Spacer(1, 6)] + safe_keep_together([t]) + [Spacer(1, 10)]

def r_quote(text):
    para = Paragraph(inline(text), S["quote"])
    t = Table([[para]], colWidths=[AVAIL_W * 0.9], hAlign="CENTER")
    t.setStyle(TableStyle([
        ("LINEBEFORE", (0, 0), (0, -1), 2, BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return [Spacer(1, 4)] + safe_keep_together([t]) + [Spacer(1, 8)]

# ---------------------------------------------------------------- doc template
class TocDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, "bookmark_name"):
            level = getattr(flowable, "bookmark_level", 0)
            text = getattr(flowable, "bookmark_text", "")
            key = getattr(flowable, "bookmark_key", "")
            self.notify("TOCEntry", (level, text, self.page, key))
            try:
                self.canv.addOutlineEntry(text, key, level=level, closed=(level > 0))
            except Exception:
                pass

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("LibSans", 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(LM, PAGE_H - 0.52 * inch, DOC_TITLE)
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(1.1)
    canvas.line(LM, PAGE_H - 0.60 * inch, PAGE_W - RM, PAGE_H - 0.60 * inch)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(LM, 0.62 * inch, PAGE_W - RM, 0.62 * inch)
    canvas.setFont("LibSans", 7.5)
    canvas.drawString(LM, 0.44 * inch, "CodingQuestions repository - Tier 1, 2 and 3 solutions")
    canvas.drawRightString(PAGE_W - RM, 0.44 * inch, "Page %d" % doc.page)
    canvas.restoreState()

# ---------------------------------------------------------------- assemble
def load_blocks(path):
    namespace = {}
    with open(path, "r", encoding="utf-8") as f:
        exec(compile(f.read(), path, "exec"), namespace)
    return namespace["BLOCKS"]

def main():
    files = sorted(
        os.path.join(CONTENT_DIR, f)
        for f in os.listdir(CONTENT_DIR)
        if re.match(r"jc\d+.*\.py$", f)
    )
    if not files:
        print("No content files found in", CONTENT_DIR)
        sys.exit(1)

    doc = TocDocTemplate(
        OUT_PDF, pagesize=A4,
        leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
        title=DOC_TITLE, author="Z.ai", creator="Z.ai",
        subject="Analysis of the CodingQuestions Java corpus: concepts, libraries, tips and tricks",
    )

    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("TOC0", fontName="LibSans-Bold", fontSize=10.5, leading=15,
                       leftIndent=0, spaceBefore=6, textColor=TEXT_PRIMARY),
        ParagraphStyle("TOC1", fontName="LibSerif", fontSize=9.8, leading=13.5,
                       leftIndent=18, textColor=TEXT_PRIMARY),
    ]

    story = []
    story.append(Paragraph("Contents", S["toc_title"]))
    story.append(HRFlowable(width="100%", thickness=1.6, color=ACCENT, spaceBefore=0, spaceAfter=10))
    story.append(toc)
    story.append(PageBreak())

    h2_counter = 0
    for path in files:
        blocks = load_blocks(path)
        for block in blocks:
            kind = block[0]
            if kind == "part":
                story += r_part(block[1], block[2])
            elif kind == "h2":
                h2_counter += 1
                story += r_h2(block[1], h2_counter)
            elif kind == "h3":
                story += r_h3(block[1])
            elif kind == "body":
                story += r_body(block[1])
            elif kind == "bullets":
                story += r_bullets(block[1])
            elif kind == "numbers":
                story += r_numbers(block[1])
            elif kind == "table":
                story += r_table(block[1])
            elif kind == "code":
                story += r_code(block[1])
            elif kind == "callout":
                story += r_callout(block[1], block[2])
            elif kind == "quote":
                story += r_quote(block[1])
            else:
                raise ValueError("Unknown block type %r in %s" % (kind, path))

    doc.multiBuild(story, onFirstPage=on_page, onLaterPages=on_page)
    print("Built", OUT_PDF)

if __name__ == "__main__":
    main()
