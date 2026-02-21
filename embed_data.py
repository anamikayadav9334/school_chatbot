import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# Load embedding model
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Load all .md files from fake_school_data folder
loader = DirectoryLoader(
    "fake_school_data",
    glob="**/*.md",
    loader_cls=TextLoader
)

documents = loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=30
)

docs = text_splitter.split_documents(documents)

# Create Chroma DB
vectorstore = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="chroma_db"
)

vectorstore.persist()

print("✅ Vector database created successfully from markdown files!")


