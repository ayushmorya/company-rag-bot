💬 Company RAG ChatbotUpload documents → Ask questions → Get grounded answers powered by Gemini + LangGraphA modern Retrieval-Augmented Generation (RAG) chatbot that allows you to upload PDFs, DOCX, and TXT files and ask natural-language questions based on their content. Built with Gemini, LangChain, LangGraph, ChromaDB, and Streamlit.Note: This project is designed as a production-style architecture, suitable for AI Engineer, ML Engineer, or GenAI portfolios.🚀 Features🔹 Document IngestionMulti-format Support: Upload multiple files (PDF, DOCX, TXT).Smart Extraction: Uses PyPDF2 and python-docx for text extraction.Chunking: Splits text into recursive chunks for optimal retrieval.Embedding: Embeds content using Google's text-embedding-004.Vector Storage: Stores vectors locally in ChromaDB.🔹 RAG ChatbotLangGraph Pipeline: Structured, stateful RAG workflow.Contextual Retrieval: Query-based retrieval from Chroma.Gemini Powered: Uses Gemini 1.5 Pro / Flash for high-quality, grounded answers.Hallucination Reduction: Answers are strictly based on uploaded context.🔹 Modern Streamlit UIChat Interface: Beautiful UI with user/bot avatars and typing animations.Sidebar Controls: Real-time file ingestion stats.Data Visibility: Displays chunk count, document count, and last update time.Session Memory: Maintains conversation history within the session.🧠 Tech StackComponentTechnologyLLMGoogle Gemini (1.5 Pro / Flash)RAG FrameworkLangGraph + LangChainEmbeddingsmodels/text-embedding-004Vector StoreChromaDBUIStreamlitBackend LogicPython 3.12📁 Project StructurePlaintextcompany-rag-bot/
│
├── app/
│   ├── config.py              # Pydantic settings / .env loader
│   ├── rag_store.py           # File ingestion, splitting, embeddings, Chroma
│   ├── rag_graph.py           # LangGraph pipeline definition
│   ├── api.py                 # (Optional) FastAPI endpoints
│   └── __init__.py
│
├── ui_streamlit.py            # 🚀 Main Streamlit Web App (UI)
├── main.py                    # (Optional) FastAPI entrypoint
│
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables (Ignored by Git)
├── .gitignore
└── README.md
🔧 Installation & Setup1️⃣ Clone the RepositoryBashgit clone https://github.com/yourusername/company-rag-bot.git
cd company-rag-bot
2️⃣ Create a Virtual EnvironmentIt is recommended to use Conda or venv to keep dependencies isolated.Bashconda create -n ragchat python=3.12 -y
conda activate ragchat
3️⃣ Install DependenciesBashpip install -r requirements.txt
4️⃣ Configure Environment VariablesCreate a .env file in the root directory and add your Google Gemini credentials.Bash# .env file
GEMINI_API_KEY="your_actual_api_key_here"
GEMINI_CHAT_MODEL="gemini-1.5-pro"  
GEMINI_EMBEDDING_MODEL="models/text-embedding-004"
(Note: Ensure you have access to the models specified).▶️ Usage GuideRun the ApplicationBashstreamlit run ui_streamlit.py
How to UseUpload Documents:Open the sidebar.Upload PDF, DOCX, or TXT files.Wait for the system to process, chunk, and embed the data.Ask Questions:Type your query in the chat input.Example: "Summarize the refund policy."Example: "What are the key skills listed in this resume?"Check Stats:View the sidebar to see how many documents and chunks are currently indexed.🤝 ContributingContributions are welcome! Please fork the repository and submit a pull request for any enhancements.📄 LicenseMIT License
