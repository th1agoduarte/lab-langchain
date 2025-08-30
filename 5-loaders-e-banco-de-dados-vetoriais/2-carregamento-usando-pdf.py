from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("./5-loaders-e-banco-de-dados-vetoriais/gpt5.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = splitter.split_documents(docs)

print(f"Total de chunks: {len(chunks)}\n")

for chunk in chunks:
    print(chunk)
    print("\n---\n")