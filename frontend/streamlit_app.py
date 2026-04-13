import streamlit as st
import requests
import os

# Configurable API URL
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("Industrial Document AI Assistant")
st.write("Ask questions about your maintenance documents.")

query = st.text_input("Enter your question")

# containers for dynamic output
answer_container = st.empty()
evidence_container = st.empty()


if st.button("Ask"):

    response = requests.post(
        f"{API_URL}/ask",
        params={"query": query}
    )

    data = response.json()

    answer = data["answer"]
    retrieved_chunks = data["evidence"]

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






