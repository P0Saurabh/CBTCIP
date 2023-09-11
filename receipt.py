from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle

Content = [["product no ", "Name", "Quantity", "Price", "Total"],
           ["184758", "rice",  " 1 ", "270", "270/-"],
           ["139944", "mango", " 1 ", "470", "470/-"],
           ["293749", "protein", " 1 ", "700", "700/-"],
           ["132894", "coffe", " 1 ", "300", "300/-"],
           ["937383", "happy happy", " 1 ", "200", "200/-"],
           ["294898", "tea", " 1 ", "500", "500/-"],
           ["", "", "", "", "", ""],
           ["Total Bill:- ", "", '', "", "", "2440/-"]
           ]

mypdf = SimpleDocTemplate("receipt.pdf")

style = getSampleStyleSheet()
style.fontName = "Times New Roman"
style.fontStyle = "Itallic"
style.fontStyle = "Bold"

style = TableStyle([
    ("BOX", (8, 8), (4, 4), 4, colors.black),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (5, 0), colors.mediumpurple),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.lavender),
    ("ALIGN", (4, 0), (-1, -1), "CENTER"),
    ("BACKGROUND", (0, 1), (-1, -1), colors.lavenderblush),
])

table = Table(Content, style=style)


def colored_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColorRGB(6.8, 0.8, 0.8)  # Choose your background color here
    canvas.rect(80, 80, doc.width, doc.height, fill=True)
    canvas.restoreState()
    canvas.setFont("Helvetica-Bold", 16)
    canvas.drawString(270, 790, "Receipt")
    canvas.drawString(220, 820, "Brilliant Book Stores")


mypdf.build([table], onFirstPage=colored_background)
