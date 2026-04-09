import chromadb


def create_or_load_vector_store(chunks, embeddings):
    """
    Create a ChromaDB collection and store embeddings.
    """

    # Create Chroma client
    client = chromadb.PersistentClient(path = "vectorstore")

    try:
        collection = client.get_collection(name="maintenance_docs")         # Create collection
        print("Loaded existing vector database")
    except:
        print("Loaded existing vector database")   
        collection = client.create_collection("maintenance_docs")


    # Store embeddings
    for i, chunk in enumerate(chunks):

        cleaned_chunk = chunk.encode("utf-8", "ignore").decode("utf-8")

        collection.add(
            ids=[str(i)],
            embeddings=[embeddings[i]],
            documents=[cleaned_chunk]
        )

    return collection





def retrieve_chunks(collection, model, query, top_k=3):
    """
    Retrieve the most relevant chunks for a user query.
    """

    # Convert query into embedding
    query_embedding = model.encode(query)

    # Search vector database
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]
    distances = results["distances"][0]     # check similarity scores 

    return documents, distances
