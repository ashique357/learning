"""
Document Ingestion Pipeline
Uses TF-IDF vectorization (scikit-learn) - no native dependencies needed
"""

import json
import pickle
from pathlib import Path
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class DocumentStore:
    def __init__(self, store_path: str = "./doc_store"):
        self.store_path = Path(store_path)
        self.chunks = []
        self.metadatas = []
        self.vectorizer = None
        self.tfidf_matrix = None

    def load(self):
        meta_file = self.store_path / "metadata.json"
        vec_file = self.store_path / "vectorizer.pkl"
        matrix_file = self.store_path / "matrix.pkl"
        if meta_file.exists() and vec_file.exists() and matrix_file.exists():
            with open(meta_file, "r") as f:
                data = json.load(f)
            self.chunks = data["chunks"]
            self.metadatas = data["metadatas"]
            with open(vec_file, "rb") as f:
                self.vectorizer = pickle.load(f)
            with open(matrix_file, "rb") as f:
                self.tfidf_matrix = pickle.load(f)
            return True
        return False

    def save(self):
        self.store_path.mkdir(parents=True, exist_ok=True)
        with open(self.store_path / "metadata.json", "w") as f:
            json.dump({"chunks": self.chunks, "metadatas": self.metadatas}, f)
        with open(self.store_path / "vectorizer.pkl", "wb") as f:
            pickle.dump(self.vectorizer, f)
        with open(self.store_path / "matrix.pkl", "wb") as f:
            pickle.dump(self.tfidf_matrix, f)

    def search(self, query: str, n_results: int = 5):
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = scores.argsort()[-n_results:][::-1]
        results = []
        for idx in top_indices:
            if scores[idx] > 0:
                results.append({
                    "text": self.chunks[idx],
                    "metadata": self.metadatas[idx],
                    "score": float(scores[idx]),
                })
        return results


class DocumentIngestion:
    def __init__(self, learning_path: str, store_path: str = "./doc_store"):
        self.learning_path = Path(learning_path)
        self.store_path = store_path
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n## ", "\n### ", "\n\n", "\n", " ", ""],
        )

    def ingest(self):
        print("🚀 Starting document ingestion...\n")
        chunks = []
        metadatas = []

        for md_file in sorted(self.learning_path.rglob("*.md")):
            try:
                content = md_file.read_text(encoding="utf-8")
                relative_path = md_file.relative_to(self.learning_path)
                subject = relative_path.parts[0] if len(relative_path.parts) > 0 else "general"

                from langchain_core.documents import Document as LCDoc
                splits = self.text_splitter.split_documents([LCDoc(page_content=content)])

                for split in splits:
                    chunks.append(split.page_content)
                    metadatas.append({
                        "subject": subject,
                        "filename": md_file.name,
                        "relative_path": str(relative_path),
                    })
                print(f"✓ Loaded: {relative_path}")
            except Exception as e:
                print(f"✗ Error: {md_file}: {e}")

        if not chunks:
            print("❌ No documents found!")
            return None

        print(f"\n📄 {len(chunks)} chunks from {len(set(m['relative_path'] for m in metadatas))} documents")
        print("🔄 Building TF-IDF index...")

        store = DocumentStore(self.store_path)
        store.chunks = chunks
        store.metadatas = metadatas
        store.vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
        store.tfidf_matrix = store.vectorizer.fit_transform(chunks)
        store.save()

        print(f"✅ Ingestion complete! Index saved to {self.store_path}")
        return store


if __name__ == "__main__":
    ingestion = DocumentIngestion("./learning-content")
    ingestion.ingest()
