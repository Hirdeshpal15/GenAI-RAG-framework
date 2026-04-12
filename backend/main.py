from fastapi import FastAPI
from backend.rag_service import process_query

app = FastAPI()


@app.get("/")
def root():
    return {"message": "RAG API is running"}


@app.post("/ask")
def ask_question(query: str):

    response = process_query(query)

    return response