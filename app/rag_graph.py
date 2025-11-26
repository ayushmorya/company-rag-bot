from __future__ import annotations

from typing import List, TypedDict

from langgraph.graph import StateGraph, END
from langchain_core.documents import Document


from .rag_store import get_chat_model, get_retriever


class RAGState(TypedDict):
    question: str
    context_docs: List[Document]
    answer: str


# Instantiate models/tools once (for performance)
_llm = get_chat_model()
_retriever = get_retriever()


def retrieve_node(state: RAGState) -> dict:
    """Retrieve relevant context from vector store."""
    question = state["question"]
    docs = _retriever.invoke(question)
    return {"context_docs": docs}


def generate_node(state: RAGState) -> dict:
    """Generate final answer using Gemini + retrieved docs."""
    question = state["question"]
    docs = state.get("context_docs", [])

    context_text = "\n\n".join(
        f"[Doc {i+1} - {d.metadata.get('source', 'unknown')}]\n{d.page_content}"
        for i, d in enumerate(docs)
    )

    system_prompt = (
        "You are a helpful company assistant. Use ONLY the provided documents to answer.\n"
        "If the answer is not clearly present, say you don't know and suggest where "
        "the user might find it.\n\n"
    )

    prompt = (
        f"{system_prompt}"
        f"Context:\n{context_text}\n\n"
        f"User question: {question}\n\n"
        "Answer in a clear, concise way. If relevant, mention which document you used."
    )

    response = _llm.invoke(prompt)
    return {"answer": response.content}


def build_rag_graph():
    """Compile and return a LangGraph graph for RAG."""
    graph = StateGraph(RAGState)

    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate", generate_node)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)

    return graph.compile()


# Pre-compiled graph ready to use
rag_graph = build_rag_graph()
