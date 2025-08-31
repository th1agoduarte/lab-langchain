import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

for k in ("OPENAI_API_KEY", "PGVECTOR_URL","PGVECTOR_COLLECTION"):
    if k not in os.environ:
        raise RuntimeError(f"Missing required environment variable: {k}")
    
query = "Tel me more about the gpt-5 thinking evaluation and performance comparing to gpt-4"

embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))

store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

results = store.similarity_search_with_score(query, k=10)
for i, (doc, score) in enumerate(results):
    print("-" * 80)
    print(f"Result {i+1} (score: {score:.4f}): \nTexto:\n \n{doc.page_content.strip()}\n")
    print(f"\nMetadata:\n \n{doc.metadata}\n")
    print("-" * 80)
