# DocGenius – Revolutionizing PDFs with AI 📄

DocGenius is an AI-powered PDF question-answering application that allows users to upload a PDF and ask questions about its contents using natural language.

The application uses a **Retrieval-Augmented Generation (RAG)** approach to find the most relevant sections of the uploaded document and generate answers based only on the retrieved content.

The current version uses **Ollama locally**, so it does not require an OpenAI API key or paid API credits.

---

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Extract text from PDFs
- ✂️ Split documents into smaller chunks
- 🧠 Generate local semantic embeddings
- 🔎 Retrieve the most relevant document sections
- 🤖 Generate answers using a local LLM
- 🔒 No OpenAI API key or paid API required
- 🚫 Prevents answers based on outside knowledge
- 💻 Runs locally using Ollama
- 🎨 Simple and interactive Streamlit interface

---

## 🧠 How It Works

DocGenius follows a **Retrieval-Augmented Generation (RAG)** pipeline:

```text
                    PDF
                     │
                     ▼
              Text Extraction
                     │
                     ▼
               Text Chunking
                     │
                     ▼
        Local Embedding Generation
          (nomic-embed-text)
                     │
                     ▼
             Vector Embeddings
                     │
                     │
User Question ──────┤
                     ▼
        Question Embedding
                     │
                     ▼
          Cosine Similarity Search
                     │
                     ▼
          Top 5 Relevant Chunks
                     │
                     ▼
              Local LLM
             (llama3.2:3b)
                     │
                     ▼
                Final Answer

```
---

## 🔍 RAG Pipeline Details

### 1. PDF Text Extraction

The uploaded PDF is processed using PyPDF2 to extract text from each page.

### 2. Text Chunking

The extracted text is divided into smaller chunks to make document processing more efficient.

### 3. Embedding Generation

Each document chunk is converted into a vector embedding using the `nomic-embed-text` model through Ollama.

### 4. Semantic Search

The user's question is also converted into an embedding. Cosine similarity is then used to find the most relevant document chunks.

### 5. Context Retrieval

The top 5 most relevant chunks are selected and combined to provide relevant context to the language model.

### 6. Answer Generation

The retrieved context and user's question are passed to the local `llama3.2:3b` language model through Ollama.

The model is instructed to answer using only the information retrieved from the uploaded document.

---

## 📁 Project Structure
```
DocGenius/
│
├── DocGenius/
│   └── PDFChat.py
│
├── Artifacts/
│   ├── Image Resources/
│   └── Outputs/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

1. Clone the Repository
```
git clone https://github.com/krutzia/DocGenius.git
cd DocGenius
```

2. Install Python Dependencies
```
pip install -r requirements.txt
```

3. Install Ollama

Download and install Ollama from:

https://ollama.com/download

Verify the installation:

```
ollama --version
```

4. Download the Required AI Models

Install the embedding model:

```
ollama pull nomic-embed-text
```

Install the language model:

```
ollama pull llama3.2:3b
```

5. Run the Application
```
streamlit run DocGenius/PDFChat.py
```

The application will be available at:

```
http://localhost:8501
```
---

## 📸 Proof of Concept

<img width="1901" height="901" alt="Image" src="https://github.com/user-attachments/assets/6e5b89bc-e613-49ef-8084-00a9bb5f559d" />

The screenshot demonstrate PDF upload, document processing, question answering, and the generated responses.

---

## 💡 Example Usage

1. Launch the application.
2. Upload a PDF document.
3. Wait for the document to be processed and embedded locally.
4. Enter a question related to the PDF.
5. DocGenius retrieves the most relevant sections using semantic similarity.
6. The local Llama 3.2 model generates an answer using the retrieved context.

### Example

**Question:**

> What is the most common customer complaint?

**Answer:**

> The most common customer complaint is the waiting time for repairs.

---

## 🛠️ Tech Stack

- **Python** — Application development
- **Streamlit** — Web interface
- **PyPDF2** — PDF text extraction
- **NumPy** — Vector operations and cosine similarity
- **Ollama** — Local AI model execution
- **nomic-embed-text** — Text embeddings
- **llama3.2:3b** — Local answer generation

---

## 🔐 Privacy

- 🔒 Uses local Ollama models for embeddings and answer generation
- 🛡️ No OpenAI API key required
- 🚫 PDF content does not need to be sent to paid external AI APIs
- 💻 Documents are processed locally on your machine

---

## 🔮 Future Improvements

- 📄 Support for multiple PDF uploads
- 💬 Conversation history and follow-up questions
- 📑 Source and page citations
- 🗄️ Persistent vector storage
- ⚡ Streaming AI responses
- ✂️ Improved document chunking
- ☁️ Cloud deployment
- 🧠 Support for larger and more capable local models


