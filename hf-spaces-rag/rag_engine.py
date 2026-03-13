"""
RAG Engine using Groq API (Free LLM)
"""

import os
from typing import List, Dict
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
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
            raise ValueError("GROQ_API_KEY not set. Add it in HF Space Settings → Secrets.")

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
        )

        self.vectorstore = Chroma(
            persist_directory=chroma_path,
            embedding_function=self.embeddings,
            collection_name="learning_docs",
        )

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

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 5}),
            chain_type_kwargs={"prompt": self.prompt},
            return_source_documents=True,
        )

    def query(self, question: str) -> Dict:
        result = self.qa_chain({"query": question})
        return {
            "answer": result["result"],
            "sources": [
                {
                    "subject": doc.metadata.get("subject", "unknown"),
                    "file": doc.metadata.get("filename", "unknown"),
                    "path": doc.metadata.get("relative_path", "unknown"),
                }
                for doc in result["source_documents"]
            ],
        }
