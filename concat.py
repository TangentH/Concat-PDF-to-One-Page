import fitz  # PyMuPDF

def concat_pdf_pages_to_one(input_pdf_path, output_pdf_path):
    # Open the input PDF
    doc = fitz.open(input_pdf_path)
    num_pages = len(doc)

    # Create a new PDF document
    new_doc = fitz.open()

    # Calculate total height and maximum width
    total_height = sum(page.rect.height for page in doc)
    max_width = max(page.rect.width for page in doc)

    # Create a new blank page with calculated dimensions
    new_page = new_doc.new_page(-1, width=max_width, height=total_height)

    # Current y-position to start inserting the next page
    current_y = 0

    # Iterate through each page and insert it into the new page
    for page in doc:
        rect = page.rect
        target_rect = fitz.Rect(0, current_y, rect.width, current_y + rect.height)  # Create a fitz.Rect for the target position
        new_page.show_pdf_page(target_rect, doc, page.number)  # Corrected page number usage
        current_y += rect.height

    # Save the new PDF
    new_doc.save(output_pdf_path)
    new_doc.close()
    doc.close()
# Example of usage
concat_pdf_pages_to_one('ResponseSummary Full.pdf', 'ResponseSummary.pdf')
