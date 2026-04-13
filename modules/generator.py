import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def generate_answer(query, retrieved_chunks):

    context = "\n".join(retrieved_chunks)

    prompt = f"""
Answer the question based ONLY on the context below.
If the answer is not in the context, say "No relevant information found."

Context:
{context}

Question:
{query}

Answer:
"""

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 300
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    return result["choices"][0]["message"]["content"]
