from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings

from classifier import classify_query
from guardrails import check_malicious
import os

from dotenv import load_dotenv
load_dotenv()

# Initialize embedding + LLM
LLM_MODEL = os.getenv("LLM_MODEL", "phi3")

embeddings = OllamaEmbeddings(model="nomic-embed-text")
llm = Ollama(model=LLM_MODEL)


# Load vector DB
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever()


def get_response(query: str):

    #  Security Check
    if check_malicious(query):
        return "⚠️ This query violates system security policies."

    # Intent Classification
    intent = classify_query(query)

    if intent == "malicious":
        return "⚠️ Suspicious request detected."

    #  Retrieve docs
    relevant_docs = retriever.invoke(query)

    if not relevant_docs:
        return "I don't know the answer to that."

    context = "\n".join([doc.page_content for doc in relevant_docs])

    prompt = f"""
You are a helpful school assistant.
Answer only using the provided context.
If answer not in context, say you don't know.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response
