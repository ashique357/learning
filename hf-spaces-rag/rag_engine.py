"""
RAG Engine using Groq API + ChromaDB built-in embeddings
No PyTorch or sentence-transformers needed
"""

import os
from typing import Dict
import chromadb
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


class RAGEngine:
    def __init__(
        self,
        chroma_path: str = "./chroma_db",
        model_name: str = "llama-3.1-8b-instant",
        temperature: float = 0.7,
    ):
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY not set. Add it in Streamlit Cloud Secrets.")

        # ChromaDB with built-in embeddings
        client = chromadb.PersistentClient(path=chroma_path)
        self.collection = client.get_collection(name="learning_docs")

        # Groq LLM
        self.llm = ChatGroq(
            model=model_name,
            temperature=temperature,
            groq_api_key=groq_api_key,
        )

        self.prompt = PromptTemplate(
            template="""You are an expert Solution Architect Learning Assistant.
Use the following context from the learning materials to answer the question comprehensively.

Context:
{context}

Question: {question}

Instructions:
- Provide detailed, accurate explanations based on the context
- Include practical examples and use cases
- Explain concepts from a Solution Architect perspective
- If the context doesn't contain enough information, say so clearly
- Structure your answer with clear sections when appropriate
- Include hands-on tips when relevant

Answer:""",
            input_variables=["context", "question"],
        )

    def query(self, question: str) -> Dict:
        # Search ChromaDB
        results = self.collection.query(query_texts=[question], n_results=5)

        # Build context from results
        context = "\n\n".join(results["documents"][0])

        # Build sources
        sources = []
        if results["metadatas"] and results["metadatas"][0]:
            for meta in results["metadatas"][0]:
                sources.append({
                    "subject": meta.get("subject", "unknown"),
                    "file": meta.get("filename", "unknown"),
                    "path": meta.get("relative_path", "unknown"),
                })

        # Query LLM
        formatted_prompt = self.prompt.format(context=context, question=question)
        response = self.llm.invoke(formatted_prompt)

        return {
            "answer": response.content,
            "sources": sources,
        }
