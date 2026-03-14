"""
RAG Engine using Groq API + TF-IDF search
No native dependencies needed
"""

import os
from typing import Dict
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from ingestion import DocumentStore


class RAGEngine:
    def __init__(
        self,
        store_path: str = "./doc_store",
        model_name: str = "llama-3.1-8b-instant",
        temperature: float = 0.7,
    ):
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY not set. Add it in Streamlit Cloud Secrets.")

        self.store = DocumentStore(store_path)
        if not self.store.load():
            raise ValueError("Document store not found. Run ingestion first.")

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

Answer:""",
            input_variables=["context", "question"],
        )

    def query(self, question: str) -> Dict:
        results = self.store.search(question, n_results=5)

        context = "\n\n".join(r["text"] for r in results)
        sources = [
            {
                "subject": r["metadata"]["subject"],
                "file": r["metadata"]["filename"],
                "path": r["metadata"]["relative_path"],
            }
            for r in results
        ]

        formatted_prompt = self.prompt.format(context=context, question=question)
        response = self.llm.invoke(formatted_prompt)

        return {"answer": response.content, "sources": sources}
