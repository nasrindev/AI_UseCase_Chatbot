import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# LLM provider selection
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")

# API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Groq model
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-13b")  # use supported model

# Optional: raise errors if keys are missing for chosen provider
if LLM_PROVIDER == "openai" and not OPENAI_API_KEY:
    raise ValueError("❌ No OpenAI API key found! Please set OPENAI_API_KEY in .env")
if LLM_PROVIDER == "groq" and not GROQ_API_KEY:
    raise ValueError("❌ No GROQ API key found! Please set GROQ_API_KEY in .env")
if LLM_PROVIDER == "gemini" and not GEMINI_API_KEY:
    raise ValueError("❌ No Gemini API key found! Please set GEMINI_API_KEY in .env")

# Web search API key (optional)
WEB_SEARCH_PROVIDER = os.getenv("WEB_SEARCH_PROVIDER", "serpapi")
WEB_SEARCH_API_KEY = os.getenv("WEB_SEARCH_API_KEY")

# Embedding model choice
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

# RAG settings
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))
TOP_K = int(os.getenv("TOP_K", 5))

# Other settings
MAX_TOKENS_RESPONSE = int(os.getenv("MAX_TOKENS_RESPONSE", 512))

# Debug: check API keys loaded
print(f"LLM_PROVIDER={LLM_PROVIDER}")
print("OpenAI key loaded:", bool(OPENAI_API_KEY))
print("Groq key loaded:", bool(GROQ_API_KEY))
print("Gemini key loaded:", bool(GEMINI_API_KEY))
