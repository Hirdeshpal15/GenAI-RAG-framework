import chromadb


def create_or_load_vector_store(chunks, embeddings):

    import chromadb

    client = chromadb.Client()

    try:
        collection = client.get_collection("rag_collection")
        print("Loaded existing vector database")

    except:
        collection = client.create_collection("rag_collection")
        print("Created new vector database")

        collection.add(
            embeddings=embeddings,
            documents=chunks,
            ids=[str(i) for i in range(len(chunks))]
        )

    return collection





def retrieve_chunks(collection, model, query, top_k=3):
    """
    Retrieve the most relevant chunks for a user query.
    """

    # Convert query into embedding
    query_embedding = model.encode([query])[0].tolist()

    # Search vector database
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]
    distances = results["distances"][0]     # check similarity scores 

    return documents, distances
