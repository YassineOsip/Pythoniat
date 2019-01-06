from reportlab.pdfgen import canvas

c = canvas.Canvas('test.pdf')
c.drawString(100,200,"yassine lafkih is coder and an artificer have natural ability to make new things and invent complicated algo to solve a lot of problems existing in our sciety")
c.save()