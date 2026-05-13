[README.md](https://github.com/user-attachments/files/27710376/README.md)
# school_chatbot<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:48CAE4&height=200&section=header&text=🏫%20School%20Chatbot&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=AI-Powered%20School%20Assistant%20%7C%20RAG%20%2B%20Ollama%20%2B%20ChromaDB&descAlignY=58&descSize=16&descColor=e0f0ff" width="100%" />

<br/>

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-phi3-FF6B35?style=for-the-badge&logo=ollama&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-8B5CF6?style=for-the-badge)
![Offline](https://img.shields.io/badge/Runs-100%25%20Offline-22C55E?style=for-the-badge&logo=shield&logoColor=white)

<br/>

> **Ask anything about your school — marks, courses, admissions — powered by RAG running fully offline.**

</div>

---

## 📽️ Demo

<div align="center">

<!-- Replace with your video link -->
[![Watch Demo](https://img.shields.io/badge/▶%20Watch%20Demo-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://drive.google.com/drive/u/0/folders/1qsDXpyFkC9R6AxF3rYx6KwDWhsUNmUtl)

</div>

---

## ✨ Features

<div align="center">

| 🔍 Smart Retrieval | 🧠 Intent Classifier | 🛡️ Guardrails | 🔒 Offline-First |
|:---:|:---:|:---:|:---:|
| ChromaDB + nomic-embed-text for semantic search | Routes queries by marks / courses / admission / general | Blocks prompt injection & malicious overrides | Runs entirely on local Ollama — no API keys |

</div>

---

## ⚡ Architecture

```
                        ┌─────────────────────────────────────┐
  User Query ──────────►│           FastAPI Backend            │
                        └────────────┬────────────────────────┘
                                     │
                          ┌──────────▼──────────┐
                          │     Guardrails       │──► ⚠️ Block
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │  Intent Classifier   │
                          │  marks/courses/      │
                          │  admission/general   │
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │  ChromaDB Retriever  │◄── nomic-embed-text
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │    Ollama (phi3)     │
                          │  Grounded Response   │
                          └──────────┬──────────┘
                                     │
                        ┌────────────▼────────────────────────┐
                        │        Browser UI (Jinja2)           │
                        └─────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Tool | Purpose |
|:---:|:---:|:---:|
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) | **FastAPI** | REST API + UI serving |
| ![Ollama](https://img.shields.io/badge/Ollama-FF6B35?style=flat-square) | **phi3** | Local LLM for generation |
| ![Embed](https://img.shields.io/badge/nomic--embed--text-8B5CF6?style=flat-square) | **nomic-embed-text** | Semantic embeddings |
| ![Chroma](https://img.shields.io/badge/ChromaDB-F59E0B?style=flat-square) | **ChromaDB** | Persistent vector store |
| ![LC](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square) | **LangChain** | RAG orchestration |
| ![HTML](https://img.shields.io/badge/HTML%2FCSS%2FJS-E34F26?style=flat-square&logo=html5&logoColor=white) | **Jinja2 Templates** | Frontend UI |

</div>

---

## 📁 Project Structure

```
school_chatbot/
├── 🚀 app.py              # FastAPI routes & server
├── 🧠 rag_engine.py       # RAG pipeline (retrieve → generate)
├── 🎯 classifier.py       # Query intent classifier
├── 🛡️  guardrails.py      # Malicious input filter
├── 📦 embed_data.py       # Embed school data → ChromaDB
├── 📂 fake_school_data/   # Sample school dataset
├── 🗄️  chroma_db/         # Persisted vector store
├── 🎨 templates/          # Jinja2 HTML UI
└── 🖼️  static/            # CSS & JS assets
```

---

## 🚀 Getting Started

### Prerequisites

![Ollama](https://img.shields.io/badge/Ollama-required-FF6B35?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)

### 1️⃣ Clone & Install

```bash
git clone https://github.com/anamikayadav9334/school_chatbot.git
cd school_chatbot
pip install -r requirements.txt
```

### 2️⃣ Pull Ollama Models

```bash
ollama pull phi3
ollama pull nomic-embed-text
```

### 3️⃣ Embed School Data

```bash
python embed_data.py
```

### 4️⃣ Launch

```bash
uvicorn app:app --reload
```

🌐 Open → **http://localhost:8000**

---

## 🔐 Security

<div align="center">

```
🛡️  Guardrails   →  Blocks system prompt injection & overrides
🎯  Classifier   →  Detects & rejects "malicious" intent queries
📚  Context-Only →  LLM answers only from retrieved school docs
```

</div>

---

## ⚙️ Configuration

Create a `.env` file to swap the LLM:

```env
LLM_MODEL=phi3   # swap to llama3, mistral, gemma, etc.
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:48CAE4,100:6C63FF&height=100&section=footer" width="100%" />

**Made  by [Anamika Yadav](https://github.com/anamikayadav9334)**



</div>
