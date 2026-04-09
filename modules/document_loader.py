from pypdf import PdfReader


def load_pdf(file_path):
    """
    Reads a PDF file and extracts text from each page.

    Args:
        file_path (str): Path to the PDF file

    Returns:
        list: A list where each item is text from one page
    """

    # Open the PDF
    reader = PdfReader(file_path)

    pages_text = []

    # Loop through all pages
    for page in reader.pages:
        text = page.extract_text()
        pages_text.append(text)

    return pages_text
    
