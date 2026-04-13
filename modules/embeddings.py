from sentence_transformers import SentenceTransformer


def create_embedding_model():

    """
    Loads the embedding model.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model

def embed_chunks(model, chunks):

    embeddings = model.encode(chunks)

    # FORCE conversion (important)
    clean_embeddings = []

    for e in embeddings:
        clean_embeddings.append(e.tolist())

    return clean_embeddings

