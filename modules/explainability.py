def show_evidence(retrieved_chunks):
    """
    Display the document chunks used to generate the answer.
    """

    print("\nEvidence used for Answer:\n")

    for i, chunk in enumerate(retrieved_chunks):
        print(f"Evidence {i+1}:")
        print(chunk)
        print("-"*60)

