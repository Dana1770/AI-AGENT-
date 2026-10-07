import requests
from knowledge_base import search_similar

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_error(error_text):
    context = search_similar(error_text)

    context_text = "\n".join(
        [f"Error: {c['error']}\nSolution: {c['solution']}" for c in context]
    )

    prompt = f"""
You are an expert Odoo developer.

Known solutions:
{context_text}

Now analyze this error and give fix:

{error_text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]