# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from models.llm import get_chatgroq_model  # or get_openai_model, get_gemini_model

app = FastAPI()

# Pydantic models for request
class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    system_prompt: str
    messages: List[ChatMessage]

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    # Choose the provider model
    chat_model = get_chatgroq_model()  # change if you want OpenAI/Gemini

    # Format messages for the model
    formatted_messages = [{"role": m.role, "content": m.content} for m in request.messages]

    try:
        # Call the model
        response_text = chat_model.invoke(formatted_messages).content
        return {"response": response_text}
    except Exception as e:
        return {"response": f"⚠️ Error: {str(e)}"}
