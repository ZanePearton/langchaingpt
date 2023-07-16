from reportlab.pdfgen import canvas

def create_pdf(text, filename):
    c = canvas.Canvas(filename)
    c.drawString(100,750,text)
    c.save()

create_pdf("Hello, World!", "hello_world.pdf")
