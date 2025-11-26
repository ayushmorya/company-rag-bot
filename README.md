🧠 Company RAG Chatbot
Upload documents → Ask questions → Get AI-grounded answers using Gemini, LangGraph, and Streamlit


📄 Overview

Company RAG Chatbot is an intelligent AI-powered document assistant that allows users to:

📥 Upload PDF, DOCX, or TXT files

🧩 Process and chunk documents

🧠 Embed them into ChromaDB

❓ Ask questions in natural language

🤖 Get grounded, RAG-based answers using Google Gemini

💬 Use an interactive Streamlit UI for chatting

This is a production-style RAG project, perfect for your portfolio, resume, or interviews.

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
1️⃣ Clone the repository
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

👉 http://localhost:8501

🧪 Usage Flow
1️⃣ Upload Files

Upload PDF, DOCX, or TXT documents from the sidebar.

2️⃣ Indexing Process

The system automatically:

Extracts text

Splits into chunks

Creates embeddings via Gemini

Stores vectors in ChromaDB

✔ Done automatically behind the scenes.

3️⃣ Chat with Your Documents

Ask questions such as:

“What skills are mentioned in the resume?”

“Summarize this policy.”

“What are the responsibilities described?”

The chatbot retrieves relevant chunks and uses Gemini to produce reliable answers.


🛠️ Deployment (Streamlit Cloud)
1. Push your project to GitHub
2. Visit:

https://share.streamlit.io

3. Create a New App

Repo: company-rag-bot

File to run:

ui_streamlit.py

4. Add secrets under Settings → Secrets
GEMINI_API_KEY="your_key_here"
GEMINI_CHAT_MODEL="gemini-1.5-pro"
GEMINI_EMBEDDING_MODEL="models/text-embedding-004"

5. Deploy 🚀

You now have a live RAG application you can share!

📝 License

This project is licensed under the MIT License.

MIT License

Copyright (c) 2025 Ayush

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS  
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL  
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR  
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,  
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR  
OTHER DEALINGS IN THE SOFTWARE.
