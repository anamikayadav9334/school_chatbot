from rag_engine import get_response

while True:
    question = input("Ask: ")
    if question.lower() == "exit":
        break
    answer = get_response(question)
    print("\nAI:", answer)

