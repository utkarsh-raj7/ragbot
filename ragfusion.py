from dotenv import load_dotenv
load_dotenv(override=True)

#setting up the gemini api client
from google import genai
genai_client = genai.Client()

import chromadb
chromadb_client = chromadb.PersistentClient(path="vector_dbs")
collection = chromadb_client.get_or_create_collection(
    name ="my_collection",
    metadata = {"description":"first database"}
)

question = input("enter your query")
while not question:
    print("invalid query")
    question = input("enter your query again")

result = collection.query(
    query_texts = [question],
    include=["documents"],
    n_results=1
)

response = genai_client.models.generate_content(
    model="gemini-3-flash-preview", contents=f"Context: {result["documents"][0]} \n\n Question: {question} \n\n Answer only using the context."
)

print(response.text)




