from groq import Groq
import os


def generate_answer(query, retrieved_chunks):

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are answering questions using ONLY the provided context.

If the answer cannot be found in the context, reply exactly:

"NO INFORMATION FOUND IN DOCUMENT."

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=300
    )

    return response.choices[0].message.content
