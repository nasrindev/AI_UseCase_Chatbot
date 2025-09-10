from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Example chatbot logic (replace with your actual chatbot function)
def get_bot_response(user_message: str) -> str:
    # Dummy response for demo
    return f"Bot reply to: {user_message}"

# Request model for /chat endpoint
class ChatRequest(BaseModel):
    message: str

# Response model for /chat endpoint
class ChatResponse(BaseModel):
    reply: str

app = FastAPI(
    title="AI UseCase Chatbot",
    description="A simple chatbot API",
    version="1.0.0"
)

# Allow CORS for all origins (optional, needed if frontend hosted elsewhere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the AI UseCase Chatbot API!"}

# Chat endpoint
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        user_message = request.message
        bot_reply = get_bot_response(user_message)
        return ChatResponse(reply=bot_reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional: health check
@app.get("/health")
def health_check():
    return {"status": "ok"}
