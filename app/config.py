import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GEMINI_API_KEY: str = (os.getenv("GEMINI_API_KEY") or "").strip()
    QDRANT_API_KEY: str = (os.getenv("QDRANT_API_KEY") or "").strip()
    QDRANT_CLUSTER_END_POINT: str = (os.getenv("QDRANT_CLUSTER_END_POINT") or "").strip()
    QDRANT_URL: str = (os.getenv("QDRANT_URL") or os.getenv("QDRANT_CLUSTER_END_POINT") or "").strip()
    QDRANT_COLLECTION: str = (os.getenv("QDRANT_COLLECTION_NAME") or "enterprise_rag").strip()
    
    GROQ_API_KEY: str = (os.getenv("GROQ_API_KEY") or "").strip()
    GROQ_MODEL_NAME: str = (os.getenv("GROQ_MODEL_NAME") or "llama-3.3-70b-versatile").strip()
    
    PORTKEY_API_KEY: str = (os.getenv("PORTKEY_API_KEY") or "").strip()
    PORTKEY_CONFIG_ID: str = (os.getenv("PORTKEY_CONFIG_ID") or "").strip()
    GROQ_SLUG: str = (os.getenv("GROQ_SLUG") or "groq-api-key").strip()
    GROQ_SLUG_FALLBACK: str = (os.getenv("GROQ_SLUG_FALLBACK") or "groq-secondary-key").strip()
    GROQ_API_KEY_FALLBACK : str = (os.getenv("GROQ_API_KEY_FALLBACK") or "").strip()
    GROQ_MODEL_NAME_FALLBACK: str = (os.getenv("GROQ_MODEL_NAME_FALLBACK") or "llama-3.3-70b-versatile").strip()
    


settings = Settings()