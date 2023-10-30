#!--encoding=utf-8--!
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def write(quizList, keyList, pdfName):
    # Create a new PDF document
    c = canvas.Canvas(pdfName, pagesize=letter)

    # Set font and font size
    c.setFont("Helvetica", 14)

    # Write content to PDF
    x_start = 50
    y_start = 700
    x = x_start
    y = y_start
    for i, content in enumerate(quizList, start=1):
        # Calculate the position for each item
        x = x_start + ((i - 1) % 3) * 200
        y = y_start - ((i - 1) // 3) * 30
        # Write the content to the PDF
        c.drawString(x, y, f"{content}")
    # Save the PDF document
    c.save()
    # Save the PDF document c.save()

