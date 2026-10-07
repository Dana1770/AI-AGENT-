from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# موديل embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

data = [
    {
        "error": "psycopg2 error column does not exist",
        "solution": "Check if field exists in model and run upgrade module"
    },
    {
        "error": "odoo xml view error",
        "solution": "Check XML syntax and ensure all fields exist"
    },
]

# تحويل لنصوص
texts = [d["error"] for d in data]
solutions = [d["solution"] for d in data]

# embeddings
embeddings = model.encode(texts)

# FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def search_similar(query):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), k=2)

    results = []
    for i in I[0]:
        results.append({
            "error": texts[i],
            "solution": solutions[i]
        })
    return results