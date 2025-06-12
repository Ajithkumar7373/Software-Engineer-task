from fastapi import FastAPI
from pydantic import BaseModel
from config import set_cors
from get_response import get_answer

app = FastAPI()
set_cors(app)

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM Chatbot API. Visit /docs to test."}

@app.post("/ask", response_model=AnswerResponse)
def answer_question(request: QuestionRequest):
    answer = get_answer(request.question)
    return {"answer": answer}
