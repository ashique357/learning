"""
Document Ingestion Pipeline for Hugging Face Spaces
"""

from pathlib import Path
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document


class DocumentIngestion:
    def __init__(self, learning_path: str, chroma_path: str = "./chroma_db"):
        self.learning_path = Path(learning_path)
        self.chroma_path = chroma_path

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n## ", "\n### ", "\n\n", "\n", " ", ""],
        )

    def load_markdown_files(self) -> List[Document]:
        documents = []
        for md_file in self.learning_path.rglob("*.md"):
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()

                relative_path = md_file.relative_to(self.learning_path)
                parts = relative_path.parts
                subject = parts[0] if len(parts) > 0 else "general"

                doc = Document(
                    page_content=content,
                    metadata={
                        "source": str(md_file),
                        "subject": subject,
                        "filename": md_file.name,
                        "relative_path": str(relative_path),
                    },
                )
                documents.append(doc)
                print(f"✓ Loaded: {relative_path}")
            except Exception as e:
                print(f"✗ Error loading {md_file}: {e}")
        return documents

    def ingest(self):
        print("🚀 Starting document ingestion...\n")
        documents = self.load_markdown_files()
        if not documents:
            print("❌ No documents found!")
            return

        chunks = self.text_splitter.split_documents(documents)
        print(f"\n📄 Created {len(chunks)} chunks from {len(documents)} documents")

        print("\n🔄 Creating vector embeddings...")
        Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.chroma_path,
            collection_name="learning_docs",
        )

        print(f"✓ Vector store created at: {self.chroma_path}")
        print(f"\n✅ Ingestion complete!")
        print(f"   Documents: {len(documents)}")
        print(f"   Chunks: {len(chunks)}")


if __name__ == "__main__":
    LEARNING_PATH = "./learning-content"
    ingestion = DocumentIngestion(LEARNING_PATH)
    ingestion.ingest()
