from dotenv import load_dotenv
import os

load_dotenv()

from modules.document_loader import load_pdf
from modules.chunking import chunk_text
from modules.embeddings import create_embedding_model, embed_chunks
from modules.retrieval import create_or_load_vector_store, retrieve_chunks
from modules.generator import generate_answer
from modules.governance import log_interaction

# Loading system ONCE 
model = None
collection = None


def initialize_system():
    global model, collection

    if model is None or collection is None:

        file_path = "data/PPE.pdf"

        pages = load_pdf(file_path)
        chunks = chunk_text(pages)

        model = create_embedding_model()
        embeddings = embed_chunks(model, chunks)

        collection = create_or_load_vector_store(chunks, embeddings)


def process_query(query):
    """
    Main RAG pipeline function
    """

    initialize_system()

    retrieved_chunks, scores = retrieve_chunks(collection, model, query)

    threshold = 1.2

    if min(scores) > threshold:
        answer = "No relevant information found in the document."
        retrieved_chunks = []

    else:
        answer = generate_answer(query, retrieved_chunks)

    log_interaction(query, answer, retrieved_chunks)

    return {
        "answer": answer,
        "evidence": retrieved_chunks
    }