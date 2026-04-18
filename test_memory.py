import chromadb
client = chromadb.PersistentClient(path="vector_dbs")
collection = client.get_or_create_collection(
    name="my_collection",
    metadata = {"description":"first database"}
)
collection.add(
    ids=["id1","id2","id3"],
    documents = ["The feline is on the mat", "dogs love bones", "Cars go fast"]
)
result = collection.query(
    query_texts = ["What do cats do?"],
    n_results=1
)
print(result["documents"])
