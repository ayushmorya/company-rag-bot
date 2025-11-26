💬 Company RAG Chatbot
Upload documents → Ask questions → Get grounded answers powered by Gemini + LangGraph

A modern Retrieval-Augmented Generation (RAG) chatbot that allows you to upload PDFs / DOCX / TXT files and ask natural-language questions based on their content.
Built with Gemini, LangChain, LangGraph, ChromaDB, and Streamlit.

This project is production-style and suitable for AI Engineer, ML Engineer, GenAI, or LLM Engineer portfolios.

🚀 Features
🔹 Document Upload (PDF, DOCX, TXT)

Upload multiple files.

Extracts text via PyPDF2 and python-docx.

Splits into recursive chunks.

Embeds using text-embedding-004 (Gemini).

Stores vectors in ChromaDB for retrieval.

🔹 RAG Chatbot

LangGraph-based RAG pipeline.

Query-based retrieval from Chroma.

Gemini 1.5 Pro / Flash for generating answers.

Answers grounded in uploaded content.

🔹 Modern Streamlit UI

Beautiful chat interface with avatars.

File ingestion sidebar with stats.

Chunk count, doc count, and updated time.

Typing animations, responsive layout.

Session-based conversation memory.

🔹 Clean Architecture

Modular folder structure.

Config management using pydantic-settings.

Clear separation of UI, backend logic, and vector store.

🧠 Tech Stack
Component	Technology
LLM	Google Gemini (1.5 Pro / Flash)
RAG Framework	LangGraph + LangChain
Embeddings	models/text-embedding-004
Vector Store	ChromaDB
UI	Streamlit
Backend Logic	Python
Deployment	Streamlit Cloud / Local


📁 Project Structure
company-rag-bot/
│
├── app/
│   ├── config.py              # Pydantic settings / .env loader
│   ├── rag_store.py           # File ingestion, splitting, embeddings, Chroma
│   ├── rag_graph.py           # LangGraph pipeline definition
│   ├── api.py                 # Optional FastAPI endpoints
│   └── __init__.py
│
├── ui_streamlit.py            # 🚀 Main Streamlit Web App (UI)
├── main.py                    # Optional FastAPI entrypoint
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env (ignored)


🔧 Installation
1️⃣ Clone repo
git clone
cd company-rag-bot

2️⃣ Create virtual environment (recommended)
conda create -n ragchat python=3.12 -y
conda activate ragchat

3️⃣ Install dependencies
pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root:
GEMINI_API_KEY="your_api_key_here"
GEMINI_CHAT_MODEL="gemini-2.5-pro"
GEMINI_EMBEDDING_MODEL="models/text-embedding-004"

▶️ Run the Streamlit App
streamlit run ui_streamlit.py



🧪 Usage Guide
1. Upload documents

Use the sidebar to upload one or multiple files.
The system will:

Extract text

Split into semantic chunks

Embed with Gemini

Save vectors in Chroma

2. Ask questions

Example prompts:

“Summarize the policies in simple points.”

“What are the key skills in the resume?”

“Extract all responsibilities mentioned.”

“What does the document say about refund policy?”

3. Check retrieval stats

You’ll see:

Number of documents

Number of chunks stored

Last updated timestamp