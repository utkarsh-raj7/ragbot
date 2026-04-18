from dotenv import load_dotenv
load_dotenv(override=True)

from google import genai
genai_client = genai.Client()

import chromadb
chromadb_client = chromadb.PersistentClient(path="vector_dbs")
collection = chromadb_client.get_or_create_collection(
    name ="my_collection",
    metadata = {"description" : "first database"}
)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    user_query = request.question
    result = collection.query(
        query_texts = [user_query],
        include = ["documents"],
        n_results = 1
    )
    answer = result["documents"][0]
    prompt = f"Context: {answer} \n\n Question: {user_query} \n\n Answer only using the context"

    response = genai_client.models.generate_content(
        model = "gemini-3-flash-preview", contents = prompt
    )

    return response.candidates[0].content.parts[0].text