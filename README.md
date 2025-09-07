# 🛍️ Retail GenAI with Neo4j & Google Agentic Development Kit (ADK)

## 📌 Project Overview
This project demonstrates how **Generative AI + Graph Databases + Agentic AI** can power **intelligent retail insights and product recommendations**.  
We integrate **Neo4j** for the retail knowledge graph, **Google Agentic Development Kit (ADK)** for multi-agent orchestration, and **Gemini Flash** for natural language generation.

---

## 🔹 Key Features
- Build a **Retail Knowledge Graph** in Neo4j (Customers, Products, Categories, Transactions, Promotions).  
- Enable **natural language querying** with agents that convert user queries → Cypher → graph insights.  
- Power **personalized recommendations** (cross-sell, seasonal promotions, customer 360 views).  
- Use **RAG (Retrieval-Augmented Generation)** with Gemini Flash to generate **marketing descriptions** enriched by graph context.  
- Validate outputs with **Eval framework** for recommendation accuracy and reliability.  

---

## 📂 Project Structure
```bash
retail-genai-neo4j-adk/
├── backend/                  # FastAPI backend service
│   ├── main.py                # API entrypoint
│   ├── routers/               # API routes
│   ├── services/              # Business logic (RAG, recommendations)
│   └── tests/                 # Unit/integration tests
├── agents/                   # Google ADK agent definitions
│   ├── query_agent.py
│   ├── recommendation_agent.py
│   └── summarization_agent.py
├── data/                     # Sample datasets (Kaggle retail, transactions, etc.)
│   └── retail_transactions.csv
├── notebooks/                # Jupyter notebooks for exploration
│   ├── graph_embedding.ipynb
│   └── recommendation_eval.ipynb
├── docker/                   # Dockerfiles, K8s manifests
│   ├── Dockerfile
│   └── k8s-deployment.yaml
├── requirements.txt          # Python dependencies
└── README.md
