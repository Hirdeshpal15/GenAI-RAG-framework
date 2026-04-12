import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import streamlit as st
from dotenv import load_dotenv

from modules.document_loader import load_pdf
from modules.chunking import chunk_text
from modules.embeddings import create_embedding_model, embed_chunks
from modules.retrieval import create_or_load_vector_store, retrieve_chunks
from modules.generator import generate_answer
from modules.explainability import show_evidence
from modules.governance import log_interaction

load_dotenv()


@st.cache_resource   # once load everything in starting
def initialize_system():

    file_path = "data/PPE.pdf"

    pages = load_pdf(file_path)
    chunks = chunk_text(pages)

    model = create_embedding_model()
    embeddings = embed_chunks(model, chunks)

    collection = create_or_load_vector_store(chunks, embeddings)

    return model, collection


st.title("Industrial Document AI Assistant")
model, collection = initialize_system()


st.write("Ask questions about your maintenance documents.")

query = st.text_input("Enter your question")

# containers for dynamic output
answer_container = st.empty()
evidence_container = st.empty()


if st.button("Ask"):

    retrieved_chunks, scores = retrieve_chunks(collection, model, query)

    # hallucination guard
    threshold = 1.2

    if min(scores) > threshold:
        answer = "No relevant information found in the document."
        retrieved_chunks = []  # IMPORTANT: clear evidence
    else:
        answer = generate_answer(query, retrieved_chunks)

    log_interaction(query, answer, retrieved_chunks)


    # Show Answer
    with answer_container.container():
        st.subheader("Answer")
        st.write(answer)


    # Show Evidence
    with evidence_container.container():

        st.subheader("Evidence")

        if retrieved_chunks:

            for i, chunk in enumerate(retrieved_chunks):
                st.markdown(f"**Evidence {i+1}**")
                st.info(chunk)

        else:
            st.write("No evidence available.")






