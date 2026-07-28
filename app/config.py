from logfire._internal.config_params import ENVIRONMENT
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GEMINI_API_KEY: str = (os.getenv("GEMINI_API_KEY") or "").strip()

    GROQ_API_KEY:str=(os.getenv("GROQ_API_KEY") or "").strip()

    QDRANT_API_KEY: str = (os.getenv("QDRANT_API_KEY") or "").strip()
    QDRANT_CLUSTER_END_POINT: str = (os.getenv("QDRANT_CLUSTER_END_POINT") or "").strip()
    QDRANT_URL: str = (os.getenv("QDRANT_URL") or os.getenv("QDRANT_CLUSTER_END_POINT") or "").strip()
    QDRANT_COLLECTION: str = (os.getenv("QDRANT_COLLECTION_NAME") or "enterprise_rag").strip()

    # Portkey configuration
    PORTKEY_API_KEY: str = (os.getenv("PORTKEY_API_KEY") or "").strip()
    PORTKEY_CONFIG_ID: str = (os.getenv("PORTKEY_CONFIG_ID") or "").strip()
    
    # Portkey virtual key identifiers
    PORTKEY_GROQ_PRIMARY_SLUG: str = (os.getenv("PORTKEY_GROQ_PRIMARY_SLUG") or "groq-production-primary-api-key").strip()
    PORTKEY_GROQ_SECONDARY_SLUG: str = (os.getenv("PORTKEY_GROQ_SECONDARY_SLUG") or "groq-production-secondary-api-key").strip()
    PORTKEY_GROQ_TERTIARY_SLUG: str = (os.getenv("PORTKEY_GROQ_TERTIARY_SLUG") or "groq-production-tertiary-api-key").strip()

    ENVIRONMENT: str = (os.getenv("ENVIRONMENT") or "production").strip()

settings = Settings()