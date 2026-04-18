from fastapi import FastAPI
app = FastAPI()

from pydantic import BaseModel
class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    user_input = request.question
    return(f"Received_Question: {user_input}, status: success")


