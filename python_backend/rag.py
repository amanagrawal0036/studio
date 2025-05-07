from database import get_player_stats
from vector_db import VectorDB
from typing import List

# Assume you're using OpenAI, adapt as needed
from openai import OpenAI
client = OpenAI()

def answer_query_with_rag(query: str, vector_db: VectorDB) -> str:
    context: List[str] = vector_db.query(query)
    prompt = f"Answer the following question using the provided context:\n\nContext:\n{chr(10).join(context)}\n\nQuestion: {query}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", # Replace with your LLM
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content