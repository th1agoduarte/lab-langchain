import os
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
current_dir = Path(__file__).parent
pdf_path = current_dir / "gpt5.pdf"

loader = PyPDFLoader(pdf_path)
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = splitter.split_documents(docs)

print(f"Total de chunks: {len(chunks)}\n")

for chunk in chunks:
    print(chunk)
    print("\n---\n")