🧠 Company RAG Chatbot
Upload documents → Ask questions → Get AI-grounded answers using Gemini, LangGraph, and Streamlit
🚀 Tech Stack & Tools
Core Technologies














Developer Tools








📄 Overview

Company RAG Chatbot is an AI-powered tool that lets users:

Upload PDF, DOCX, or TXT files

Store embedded chunks in ChromaDB

Query the knowledge base in natural language

Receive LLM-grounded answers generated through Google Gemini

Interact through a clean, modern Streamlit UI

This is a resume-ready, production-style RAG project built with best practices in architecture and design.

🗂️ Project Structure
company-rag-bot/
│
├── app/
│   ├── config.py              # Env variables & settings (pydantic-settings)
│   ├── rag_store.py           # File processing, embedding, and vector DB
│   ├── rag_graph.py           # LangGraph workflow for RAG
│   ├── api.py                 # (Optional) FastAPI endpoints
│   └── __init__.py
│
├── ui_streamlit.py            # Streamlit Frontend UI
├── main.py                    # FastAPI entrypoint (optional)
│
├── requirements.txt
├── README.md
└── .env (ignored)

🔧 Installation & Setup
1️⃣ Clone this repository
git clone https://github.com/<your-username>/company-rag-bot.git
cd company-rag-bot

2️⃣ Create a fresh environment
conda create -n ragchat python=3.12 -y
conda activate ragchat

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create a .env file
GEMINI_API_KEY="your_api_key_here"
GEMINI_CHAT_MODEL="gemini-1.5-pro"
GEMINI_EMBEDDING_MODEL="models/text-embedding-004"

▶️ Run the App (Streamlit)
streamlit run ui_streamlit.py


Your app will open at:

http://localhost:8501

🧪 Usage Flow
1. Upload files

Add PDF, DOCX, or TXT documents in the sidebar.

2. Indexing

The system:

Extracts text

Splits into chunks

Creates embeddings

Stores embeddings in ChromaDB

3. Chat

Ask questions such as:

“What skills are mentioned in the resume?”

“Summarize this policy.”

“Tell me responsibilities listed in the document.”

The bot retrieves relevant chunks using vector similarity and sends them to Gemini for grounded answering.

📸 Screenshots (Add yours)
Upload & Chat Interface

(Add screenshot here)

RAG Stats Panel

(Add screenshot here)

🛠️ Deployment (Streamlit Cloud)

Push your code to GitHub

Visit https://share.streamlit.io

Add new app → Select repo

File to run:

ui_streamlit.py


Add secrets under Settings → Secrets:

GEMINI_API_KEY="your_key_here"
GEMINI_CHAT_MODEL="gemini-1.5-pro"
GEMINI_EMBEDDING_MODEL="models/text-embedding-004"


Deploy and share!
