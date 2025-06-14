# 🛡️ AI-Powered Threat Detection and Response Chatbot

An intelligent cybersecurity assistant that combines **AI**, **RAG (Retrieval-Augmented Generation)**, and **real-world threat intelligence** to help users detect, understand, and mitigate malware, ransomware, and other cyber threats.

> 💬 Ask anything like:
> - “What is Emotet ransomware?”
> - “How to mitigate fileless attacks?”
> - “Explain MITRE technique T1055”
> - “What tools does APT28 use?”

---

## 🚀 Features

- 💬 **Chatbot Interface** – Intuitive UI built with React.js
- 🧠 **RAG-based Contextual Search** – Retrieves relevant threat info from cybersecurity documents
- 🔐 **Threat & Malware Intelligence** – Powered by data from MITRE ATT&CK, CVE, Malpedia, and more
- 🛡️ **Remediation Assistant** – Provides actionable mitigation and detection strategies
- ⚙️ **MERN Stack Architecture** – Scalable and modern full-stack solution

---

## 🧰 Tech Stack

| Component   | Technology |
|-------------|------------|
| Frontend    | React.js |
| Backend     | Express.js + Node.js |
| Database    | MongoDB / MongoDB Atlas (with optional Vector Search) |
| Vector DB   | FAISS / Pinecone / MongoDB Atlas Vector Search |
| Embedding   | `text-embedding-ada-002` (via OpenAI or Azure) |
| LLM         | Azure OpenAI / OpenAI GPT-3.5 or GPT-4 |
| Integration | LangChain.js or Python microservice (for RAG) |

---

## 📚 Data Sources

- [MITRE ATT&CK](https://attack.mitre.org/) – Techniques, groups, mitigations
- [CVE Details](https://www.cvedetails.com/) – Vulnerability and CVSS data
- [Malpedia](https://malpedia.caad.fkie.fraunhofer.de/) – Malware family insights
- [VirusTotal / VirusShare] – Sample behavior and metadata
- Security blogs – (Optional: can be parsed and ingested)

---

## 🔄 System Workflow

```plaintext
[User Query]
     ↓
[React Chat UI]
     ↓
[Express API - /ask]
     ↓
[Vector DB (FAISS/Pinecone)]
     ↓
[Fetch relevant documents]
     ↓
[Send to LLM (Azure OpenAI/GPT)]
     ↓
[Return detailed response]
     ↓
[Display in React UI]
