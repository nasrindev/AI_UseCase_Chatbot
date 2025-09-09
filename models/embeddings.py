# models/embeddings.py
from config.config import EMBEDDING_MODEL, OPENAI_API_KEY
import os

# Example using OpenAI. For other providers, add conditionals.
def get_embedding(text: str) -> list:
    """
    Returns vector embedding for a single text.
    """
    try:
        import openai
        openai.api_key = OPENAI_API_KEY
        resp = openai.Embeddings.create(
            model=EMBEDDING_MODEL,
            input=text
        )
        return resp["data"][0]["embedding"]
    except Exception as e:
        # Log and raise so the caller can handle gracefully
        raise RuntimeError(f"Embedding error: {e}")
