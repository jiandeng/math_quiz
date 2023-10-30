#!--encoding=utf-8--!
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from math import ceil

number_columns = 3
quiz_height = 30
top_margin = 60
left_margin = 40

# Function to set quiz size
def set_layout(columns_per_line, height_of_row):
    global number_columns, quiz_height
    number_columns = columns_per_line
    quiz_height = height_of_row

def set_margin(top, left):
    global top_margin, left_margin
    top_margin = top
    left_margin = left

def write(quizList, keyList, pdfName):
    # Create a new PDF document
    c = canvas.Canvas(pdfName, pagesize=letter)

    # Set font and font size
    c.setFont("Helvetica", 14)

    # Calculate page dimensions
    page_width, page_height = letter
    usable_page_width = page_width - 2 * left_margin
    usable_page_height = page_height - 2 * top_margin

    # Calculate number of rows
    number_rows = int(usable_page_height / quiz_height)

    # Calculate quiz width
    quiz_width = (usable_page_width / number_columns)

    # Calculate number of quizzes per page
    quizzes_per_page = int(usable_page_height / quiz_height) * number_columns
    total_pages = ceil(len(quizList) / quizzes_per_page)

    # Write content to PDF
    x_start = left_margin
    y_start = page_height - top_margin
    x = x_start
    y = y_start
    page_number = 1
    for i, content in enumerate(quizList, start=1):
        # Calculate the position for each item
        x = x_start + (((i - 1) - (page_number - 1) * quizzes_per_page) % 3) * quiz_width
        y = y_start - (((i - 1) - (page_number - 1) * quizzes_per_page) // 3) * quiz_height
        # Write the content to the PDF
        c.drawString(x, y, f"{content}")

        # Check if the current page is full
        if i % quizzes_per_page == 0:
            # Add page number to the current page
            c.drawString(page_width - 50, 10, f"{page_number}/{total_pages}")
            # Add meta data to the current pate
            c.drawString(100, 30, f"Date:___________")
            c.drawString(240, 30, f"Score:___________")
            c.drawString(380, 30, f"Time:___________")
            # Save the current page and start a new one
            c.showPage()
            page_number += 1

    # Add page number to the last page
    c.drawString(page_width - 50, 10, f"{page_number}/{total_pages}")
    # Add meta data to the last page
    c.drawString(100, 30, f"Date:___________")
    c.drawString(240, 30, f"Score:___________")
    c.drawString(380, 30, f"Time:___________")

    # Save the PDF document
    c.save()

