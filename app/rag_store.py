from __future__ import annotations

from pathlib import Path
from typing import List

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.documents import Document

from .config import get_settings

from PyPDF2 import PdfReader
import docx


settings = get_settings()


def get_embedding_model() -> GoogleGenerativeAIEmbeddings:
    """Return Gemini embedding model."""
    return GoogleGenerativeAIEmbeddings(
        model=settings.gemini_embedding_model,
        google_api_key=settings.gemini_api_key,
    )


def get_chat_model() -> ChatGoogleGenerativeAI:
    """Return Gemini chat model."""
    return ChatGoogleGenerativeAI(
        model=settings.gemini_chat_model,
        google_api_key=settings.gemini_api_key,
        temperature=0.2,
    )


def get_vectorstore() -> Chroma:
    """Create / load persistent Chroma vectorstore."""
    embeddings = get_embedding_model()
    vectordb = Chroma(
        embedding_function=embeddings,
        persist_directory=str(settings.vectordb_dir),
    )
    return vectordb


# ---------- Document loading helpers ----------

def load_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def load_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load_docx(path: Path) -> str:
    doc = docx.Document(str(path))
    return "\n".join([p.text for p in doc.paragraphs])


def load_file_to_text(path: Path) -> str:
    """Read supported file types into plain text."""
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return load_pdf(path)
    elif suffix == ".txt":
        return load_txt(path)
    elif suffix in [".docx", ".doc"]:
        return load_docx(path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")


def split_text_to_docs(text: str, source: str) -> List[Document]:
    """Split raw text into small chunks with metadata."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        length_function=len,
    )
    docs = splitter.create_documents(
        texts=[text],
        metadatas=[{"source": source}],
    )
    return docs


def ingest_file(file_path: Path) -> int:
    """
    Ingest a single file into vector DB.
    Returns number of chunks added.
    """
    text = load_file_to_text(file_path)
    docs = split_text_to_docs(text, source=str(file_path.name))
    vectordb = get_vectorstore()
    vectordb.add_documents(docs)
    vectordb.persist()
    return len(docs)


def get_retriever(k: int = 5):
    vectordb = get_vectorstore()
    return vectordb.as_retriever(search_kwargs={"k": k})
