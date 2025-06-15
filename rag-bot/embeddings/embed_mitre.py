import pandas as pd
import numpy as np
import faiss
from langchain.embeddings import OpenAIEmbeddings

# Load data
df = pd.read_csv("mitre.csv")
docs = df['description'].tolist()

# Azure OpenAI config
embeddings = OpenAIEmbeddings(
    deployment="embedding-deployment",
    model="text-embedding-ada-002",
    openai_api_base="https://YOUR-ENDPOINT",
    openai_api_key="YOUR-KEY"
)

# Generate embeddings
vectors = embeddings.embed_documents(docs)

# Save index with FAISS
index = faiss.IndexFlatL2(len(vectors[0]))
index.add(np.array(vectors).astype("float32"))

# Save both index and docs
faiss.write_index(index, "mitre_index.faiss")
df.to_csv("mitre_texts.csv", index=False)

print("✅ Embeddings & FAISS index created successfully.")
