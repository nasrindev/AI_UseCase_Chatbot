import os
import sys
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# --------- GROQ ---------
def get_chatgroq_model():
    """Initialize and return the Groq chat model"""
    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        groq_model = ChatGroq(
            api_key=api_key,
            model="llama-3.3-70b-versatile"  # Updated model
        )
        return groq_model
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Groq model: {str(e)}")

# --------- OPENAI ---------
def get_openai_model():
    """Initialize and return the OpenAI chat model"""
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        openai_model = ChatOpenAI(
            api_key=api_key,
            model="gpt-4o-mini"  # default, can change
        )
        return openai_model
    except Exception as e:
        raise RuntimeError(f"Failed to initialize OpenAI model: {str(e)}")

# --------- GEMINI ---------
def get_gemini_model():
    """Initialize and return the Google Gemini chat model"""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        gemini_model = ChatGoogleGenerativeAI(
            api_key=api_key,
            model="gemini-1.5-pro"  # default, can change
        )
        return gemini_model
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Gemini model: {str(e)}")
