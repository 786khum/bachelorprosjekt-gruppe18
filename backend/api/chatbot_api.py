from fastapi import FastAPI
from pydantic import BaseModel
from core.model_handler import generate_answer

app = FastAPI(
    title="Chatbot API",
    description="Backend for KI chatbot bachelorprosjekt",
    version="1.0"
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    response = generate_answer(request.message)
    return {"response": response}
