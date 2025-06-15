from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import faiss
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings

app = Flask(__name__)

# Load saved data
index = faiss.read_index("mitre_index.faiss")
data = pd.read_csv("mitre_texts.csv")

# Azure OpenAI setup
llm = ChatOpenAI(
    deployment_name="gpt-deployment",
    model_name="gpt-35-turbo",
    openai_api_base="https://YOUR-ENDPOINT",
    openai_api_key="YOUR-KEY"
)

emb = OpenAIEmbeddings(
    deployment="embedding-deployment",
    model="text-embedding-ada-002",
    openai_api_base="https://YOUR-ENDPOINT",
    openai_api_key="YOUR-KEY"
)

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json['question']
    q_vec = emb.embed_query(query)
    D, I = index.search(np.array([q_vec]), k=3)
    
    context = "\n\n".join(data.iloc[i]['description'] for i in I[0])
    prompt = f"Answer the following question using the info:\n\n{context}\n\nQ: {query}\nA:"
    answer = llm.predict(prompt)
    
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(port=5002)
