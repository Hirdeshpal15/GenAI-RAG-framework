

def clean_text(text):
    return text.encode("utf-8", "ignore").decode("utf-8")



def chunk_text(pages, chunk_size=500, overlap=50):
    """
    Splits pages of text into smaller overlapping chunks.

    Args:
        pages (list): List of page texts
        chunk_size (int): Size of each chunk
        overlap (int): Overlap between chunks

    Returns:
        list: List of text chunks
    """    

    chunks = []

    for page in pages:
        text = clean_text(page)   # ✅ IMPORTANT

        for i in range(0, len(text), chunk_size - overlap):
            chunk = text[i:i + chunk_size]
            chunks.append(chunk)

    return chunks