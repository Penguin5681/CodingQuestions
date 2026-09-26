from pypdf import PdfReader, PdfWriter, Transformation

A4_W, A4_H = 595.28, 841.89

def normalize_page_to_a4(page):
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    if abs(w - A4_W) > 2 or abs(h - A4_H) > 2:
        sx, sy = A4_W / w, A4_H / h
        page.add_transformation(Transformation().scale(sx=sx, sy=sy))
        page.mediabox.lower_left = (0, 0)
        page.mediabox.upper_right = (A4_W, A4_H)
    return page

writer = PdfWriter()
writer.add_page(normalize_page_to_a4(PdfReader("cover.pdf").pages[0]))
for page in PdfReader("body.pdf").pages:
    writer.add_page(normalize_page_to_a4(page))
writer.add_metadata({
    "/Title": "Java Source Code Analysis - Tips, Tricks and Concepts",
    "/Author": "Z.ai",
    "/Creator": "Z.ai",
    "/Subject": "Analysis of the CodingQuestions Java corpus: libraries, concepts, sorting patterns, tips and tricks",
})
with open("final.pdf", "wb") as f:
    writer.write(f)
print("merged: final.pdf")
