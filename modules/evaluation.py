def evaluate_relevance(query, retrieved_chunks):
    """
    Measures how relevant retrieved chunks are to the query
    """

    query_words = query.lower().split()
    matches = 0

    for chunk in retrieved_chunks:
        for word in query_words:
            if word in chunk.lower():
                matches += 1

    return matches / (len(query_words) * len(retrieved_chunks) + 1)


def evaluate_faithfulness(answer, retrieved_chunks):
    """
    Measures how grounded the answer is in retrieved chunks
    """

    context = " ".join(retrieved_chunks).lower()
    answer_words = answer.lower().split()

    matches = sum(1 for word in answer_words if word in context)

    return matches / (len(answer_words) + 1)