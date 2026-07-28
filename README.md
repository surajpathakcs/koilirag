# Fonepay AI Assistant (Agentic RAG)

An advanced Agentic RAG (Retrieval-Augmented Generation) chatbot designed specifically for Fonepay. This assistant uses LangGraph to route queries, NeMo Guardrails for safety, and Qdrant for vector search. It is fine-tuned to answer technical and onboarding questions regarding Fonepay Hardware, APIs, and Merchant Services.

## 🚀 Quickstart (Docker)

The easiest way to run the entire stack (API, Streamlit UI, and Qdrant) is via Docker Compose:

```bash
# Start all services in the background
docker-compose up -d

# View logs for all services
docker-compose logs -f

# Stop all services
docker-compose down
```

## 🛠️ Local Development Setup

If you prefer to run the API and UI directly on your host machine:

### 1. Python Environment Setup
First, create a virtual environment and install dependencies:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Mac/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Start Qdrant Vector Database
Qdrant is required for document ingestion and retrieval. Run it via Docker:
```bash
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

### 2. Environment Variables
Ensure your `.env` file is set up in the root directory. Required variables:
```ini
QDRANT_URL=http://localhost:6333
# Add API keys for LLM providers (e.g., Groq, Portkey)
```

### 3. Data Ingestion
To parse, embed, and index the Fonepay HTML and PDF corpus into Qdrant:
```bash
# Ingest the Fonepay data directory (will wipe existing indices)
python -m app.ingestion.processor data/fonepay --wipe
```

### 4. Run the Backend API (FastAPI)
```bash
python -m uvicorn app.main:app --reload --port 8000
```

### 5. Run the Frontend UI (Streamlit)
```bash
python -m streamlit run ui/app.py
```

## 🏗️ Architecture
- **Guardrails**: NeMo Guardrails intercepts off-topic and malicious prompts.
- **Planner (Contextualizer)**: A LangGraph node that rewrites conversational questions into standalone vector search queries using chat history.
- **Retriever**: Fetches chunks from Qdrant and uses FlashRank (Cross-Encoder) for high-precision semantic reranking.
- **Responder**: Synthesizes the final answer using the reranked context and provides inline citations.