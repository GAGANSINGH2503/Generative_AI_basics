# Generative_AI_basics
This repository is a complete guide to Generative AI, covering everything from core fundamentals to advanced topics. Ideal for beginners and experienced developers alike, it includes hands-on examples and clear explanations to help you build and understand modern AI systems.

# start-1.py file 
# 🧠 Text Generator with Ollama LLM

This is a simple Python script that uses the [Ollama](https://ollama.com) Local LLM API to generate **funny responses** to a custom prompt using `llama3`.

## 🚀 Features

- Connects to a local Ollama LLM (`llama3`)
- Sends a prompt and receives generated text
- Streams the response in real-time
- Easily customizable

## 🛠️ Requirements

- Python 3.7+
- [Ollama installed & running locally](https://ollama.com/download)
- `llama3` model pulled via:
  ```bash
  ollama run llama3


# pdf-rag.py file 
##  Contents
## 🧠 PDF-RAG with Ollama and LangChain
This project builds an AI-powered assistant capable of answering questions from a PDF document using a Retrieval-Augmented Generation (RAG) pipeline. It combines the power of LangChain, Ollama, and local language models to create a smart, context-aware system that reads documents and responds intelligently to user queries.

## 🔍 What It Does
📄 Loads a PDF file from your local system.

✂️ Splits the content into manageable chunks using a recursive text splitter, ensuring overlapping context is preserved.

🧬 Embeds each chunk into a vector space using nomic-embed-text via Ollama.

🧠 Stores the embeddings in a Chroma vector database.

❓ Accepts a user question, and with the help of a prompt-enhanced MultiQueryRetriever, it:

Generates multiple semantically relevant sub-questions.

Retrieves matching chunks from the PDF.

🗣️ Feeds the retrieved context and user question into a local language model like llama3 through Ollama.

💡 Generates answers based solely on the content of the document, ensuring relevance and grounded responses.

##  💼 Use Case
Ideal for:

Summarizing research papers

Answering regulatory or compliance-related queries

Extracting key business or legal insights

Building document-based virtual assistants

## 🧰 Tools & Technologies
LangChain – for building the RAG pipeline

Ollama – to run local LLMs and embedding models

nomic-embed-text – for generating vector representations

llama3 – as the local chat model for intelligent answer generation

Chroma – for storing and querying vectorized documents

## ⚙️ How It Works (Flow)
Ingestion: PDF is loaded and converted into text.

Chunking: The text is split into overlapping segments to preserve context.

Embedding: Each chunk is turned into a vector using a locally running embedding model.

Storage: Vectors are stored in a persistent Chroma DB.

Querying: User question is broken into sub-questions; the most relevant chunks are retrieved.

Answering: A local LLM generates a response using the retrieved content only.

## 📝 Output
When you run the project, it prints:

A preview of the document

Confirmation of successful chunking and vector DB insertion

Detailed answers to your queries generated from the PDF
