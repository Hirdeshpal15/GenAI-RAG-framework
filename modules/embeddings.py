from sentence_transformers import SentenceTransformer


def create_embedding_model():

    """
    Loads the embedding model.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model




def embed_chunks(model, chunks):

    """
    Converts text chunks into embeddings.

    Args:
        model: embedding model
        chunks (list): list of text chunks

    Returns:
        list: embeddings
    """

    embeddings = model.encode(chunks)
    return embeddings


