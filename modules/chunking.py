

def chunk_text(pages, chunck_size= 500, overlap = 100):
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
        start = 0
        while start < len(pages):
            end = start + chunck_size
            chunk = page[start:end]
            chunks.append(chunk)
            start += chunck_size-overlap

    return chunks