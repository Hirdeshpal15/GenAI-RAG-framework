# Industrial Document AI Assistant (RAG System)

## 📌 Overview

This project is an end-to-end **Retrieval-Augmented Generation (RAG)** system designed to answer questions from industrial documents with high accuracy, explainability, and reduced hallucination.

The system combines **vector search (ChromaDB)** with **LLM-based generation** to provide context-aware answers along with supporting evidence.

---

## Features

* 📄 PDF document ingestion and processing
* ✂️ Intelligent text chunking
* 🔎 Semantic search using embeddings (Sentence Transformers)
* 🧠 LLM-based answer generation (Groq API)
* 📊 Explainability via evidence chunks
* 🚫 Hallucination control using similarity thresholds
* 📈 Evaluation metrics (Relevance & Faithfulness)
* 🗂️ Interaction logging (SQLite)
* ⚡ FastAPI backend
* 🎨 Streamlit frontend
* 🐳 Docker containerization
* 🔄 CI/CD pipeline (GitHub Actions)
* ☁️ Cloud deployment (Azure App Service)

---

## 🏗️ Architecture

```
User (Streamlit UI)
        ↓
FastAPI Backend (Azure)
        ↓
RAG Pipeline
   ↓         ↓
Retriever   Generator
(ChromaDB)  (LLM - Groq)
        ↓
Response + Evidence
```

---

## How It Works

1. **Document Ingestion**

   * PDF is loaded and split into smaller chunks.

2. **Embedding Generation**

   * Each chunk is converted into vector embeddings.

3. **Vector Storage**

   * Embeddings stored in ChromaDB.

4. **Query Processing**

   * User query is converted into embedding.

5. **Retrieval**

   * Top relevant chunks are retrieved using similarity search.

6. **Generation**

   * LLM generates answer using retrieved context.

7. **Explainability**

   * Evidence chunks are shown alongside the answer.

---

## Project Structure

```
genai_framework_project/
│
├── backend/                # FastAPI backend
├── frontend/               # Streamlit UI
├── modules/                # Core logic (RAG pipeline)
├── data/                   # Input documents
├── database/               # Logs storage
├── vectorstore/            # Vector DB (ignored in git)
│
├── .github/workflows/      # CI/CD pipeline
├── Dockerfile              # Container setup
├── requirements.txt
├── README.md
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/genai-framework-project.git
cd genai-framework-project
```

---

### 2. Create Environment

```bash
conda create -n dev python=3.10
conda activate dev
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## Run Locally

### Start Backend

```bash
uvicorn backend.main:app --reload
```

---

### Start Frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

## Docker Usage

### Build Image

```bash
docker build -t rag-app .
```

---

### Run Container

```bash
docker run -p 8000:8000 --env-file .env rag-app
```

---

## Deployment

* Backend deployed on **Azure App Service**
* Docker image hosted on **Docker Hub**
* CI/CD pipeline using **GitHub Actions**

---

## Evaluation Metrics

The system evaluates performance using:

* **Relevance Score** → Measures quality of retrieved chunks
* **Faithfulness Score** → Measures grounding of generated answer

---

## Hallucination Control

* Uses similarity threshold to detect irrelevant retrieval
* Returns fallback response when confidence is low

---

## Key Learnings

* Handling embedding inconsistencies
* Managing dependency conflicts (Torch, Transformers)
* Debugging API integration issues
* Designing production-ready GenAI systems

---

## Future Improvements

* Multi-document upload support
* Hybrid search (BM25 + vector)
* Authentication system
* Monitoring dashboard

---

## 👤 Author

**Hirdeshpal**

---

## ⭐ If you found this useful, consider giving a star!
