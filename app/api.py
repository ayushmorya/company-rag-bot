from __future__ import annotations

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi import Depends
from fastapi import Body
from pydantic import BaseModel
from pathlib import Path
import shutil

from .config import get_settings
from .rag_store import ingest_file
from .rag_graph import rag_graph

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@router.post("/upload")
async def upload_document(file: UploadFile = File(...), settings=Depends(get_settings)):
    """
    Upload a document (PDF, TXT, DOCX). It will be ingested into the vector DB.
    """
    allowed_exts = {".pdf", ".txt", ".docx", ".doc"}
    suffix = Path(file.filename).suffix.lower()

    if suffix not in allowed_exts:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {suffix}. Allowed: {allowed_exts}",
        )

    # Save to data directory
    dest_path = settings.data_dir / file.filename
    with dest_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Ingest into vector DB
    try:
        chunks = ingest_file(dest_path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "File uploaded and ingested", "chunks_added": chunks}


@router.post("/chat", response_model=ChatResponse)
async def chat_with_docs(payload: ChatRequest = Body(...)):
    """
    Ask a question. The bot will answer based on uploaded documents.
    """
    state = {"question": payload.question}
    result = rag_graph.invoke(state)
    answer = result["answer"]
    return ChatResponse(answer=answer)


@router.get("/health")
async def health_check():
    return {"status": "ok"}
