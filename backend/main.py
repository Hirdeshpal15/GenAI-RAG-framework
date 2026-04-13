from fastapi import FastAPI
from fastapi.responses import JSONResponse
from backend.rag_service import process_query

app = FastAPI()


@app.get("/")
def root():
    return {"message": "RAG API is running"}


@app.post("/ask")
def ask(query: str):

    result = process_query(query)

    return JSONResponse(content=result)