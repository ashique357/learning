"""
Document Ingestion Pipeline
Uses ChromaDB's built-in embeddings (no PyTorch needed)
"""

from pathlib import Path
from typing import List
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentIngestion:
    def __init__(self, learning_path: str, chroma_path: str = "./chroma_db"):
        self.learning_path = Path(learning_path)
        self.chroma_path = chroma_path
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n## ", "\n### ", "\n\n", "\n", " ", ""],
        )

    def load_markdown_files(self) -> List[dict]:
        documents = []
        for md_file in self.learning_path.rglob("*.md"):
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()
                relative_path = md_file.relative_to(self.learning_path)
                parts = relative_path.parts
                subject = parts[0] if len(parts) > 0 else "general"
                documents.append({
                    "content": content,
                    "subject": subject,
                    "filename": md_file.name,
                    "relative_path": str(relative_path),
                })
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

        # Split documents into chunks
        all_texts = []
        all_metadatas = []
        all_ids = []
        chunk_id = 0

        for doc in documents:
            from langchain_core.documents import Document as LCDoc
            lc_doc = LCDoc(page_content=doc["content"])
            chunks = self.text_splitter.split_documents([lc_doc])

            for chunk in chunks:
                all_texts.append(chunk.page_content)
                all_metadatas.append({
                    "subject": doc["subject"],
                    "filename": doc["filename"],
                    "relative_path": doc["relative_path"],
                })
                all_ids.append(f"chunk_{chunk_id}")
                chunk_id += 1

        print(f"\n📄 Created {len(all_texts)} chunks from {len(documents)} documents")
        print("\n🔄 Creating vector embeddings...")

        # Use ChromaDB directly with built-in embeddings
        client = chromadb.PersistentClient(path=self.chroma_path)

        # Delete existing collection if exists
        try:
            client.delete_collection("learning_docs")
        except Exception:
            pass

        collection = client.create_collection(name="learning_docs")
        
        # Add in batches of 50
        batch_size = 50
        for i in range(0, len(all_texts), batch_size):
            end = min(i + batch_size, len(all_texts))
            collection.add(
                documents=all_texts[i:end],
                metadatas=all_metadatas[i:end],
                ids=all_ids[i:end],
            )

        print(f"✓ Vector store created at: {self.chroma_path}")
        print(f"\n✅ Ingestion complete!")
        print(f"   Documents: {len(documents)}")
        print(f"   Chunks: {len(all_texts)}")


if __name__ == "__main__":
    LEARNING_PATH = "./learning-content"
    ingestion = DocumentIngestion(LEARNING_PATH)
    ingestion.ingest()
