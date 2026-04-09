import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from dotenv import load_dotenv
load_dotenv()

from modules.document_loader import load_pdf
from modules.chunking import chunk_text
from modules.embeddings import create_embedding_model, embed_chunks
from modules.retrieval import create_or_load_vector_store, retrieve_chunks
from modules.generator import generate_answer
from modules.explainability import show_evidence
from modules.governance import log_interaction



file_path = "data/PPE.pdf"


# Load document
pages = load_pdf(file_path)


# Chunk document
chunks = chunk_text(pages)


# Create embeddings
model = create_embedding_model()
embeddings = embed_chunks(model, chunks)


# Store vectors
collection = create_or_load_vector_store(chunks, embeddings)


# Ask question
query = "What are the PPE assessment guidelines?"
retrieved_chunks, scores = retrieve_chunks(collection, model, query)


# Generate content
answer = generate_answer(query, retrieved_chunks)


print("\nUser Question:")
print(query)

print("\nAI Answer:")
print(answer)



# Explainability (Evidence)
show_evidence(retrieved_chunks)


# Log Interactons
log_interaction(query, answer, retrieved_chunks)












# pages = load_pdf(file_path)                             # Load document
# chunks = chunk_text(pages)                              # Chunk document
# model = create_embedding_model()                        # Load embedding model
# embeddings = embed_chunks(model, chunks)                # Create embeddings
# collection = create_vector_store(chunks, embeddings)    # Store in vector DB
# query = "What is the turbine maintenance interval?"     # Ask a question
# results = retrieve_chunks(collection, model, query)     # retreive answer