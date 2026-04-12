from backend.rag_service import process_query

query = "What are PPE requirements?"

response = process_query(query)

print("\nAnswer:")
print(response["answer"])

print("\nEvidence:")
for e in response["evidence"]:
    print("-", e[:100])