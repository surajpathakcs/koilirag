"""
Production-grade HTTP Client for interacting with the FastAPI Backend.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import requests
import logging

logger = logging.getLogger(__name__)

@dataclass
class QueryResponse:
    question: str
    answer: str
    thought_process: List[str] = field(default_factory=list)
    status: str = "success"
    sources: List[Dict[str, Any]] = field(default_factory=list)
    error_message: Optional[str] = None

class RAGApiClient:
    """
    HTTP Client managing API requests to the Fonepay AI Assistant FastAPI server.
    """
    def __init__(self, base_url: str, timeout: int = 60):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "Fonepay-RAG-Streamlit-UI/1.0"
        })

    def check_health(self) -> bool:
        """
        Pings the root GET endpoint to verify backend connectivity.
        """
        try:
            response = self.session.get(f"{self.base_url}/", timeout=5)
            return response.status_code == 200
        except Exception as e:
            logger.warning(f"Backend health check failed: {e}")
            return False

    def send_query(self, query: str, thread_id: str = "default_user") -> QueryResponse:
        """
        Sends a user query to the /query endpoint.
        """
        payload = {
            "q": query,
            "thread_id": thread_id
        }
        try:
            response = self.session.post(
                f"{self.base_url}/query",
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            
            return QueryResponse(
                question=data.get("question", query),
                answer=data.get("answer", "No answer returned from server."),
                thought_process=data.get("thought_process", []),
                status=data.get("status", "completed"),
                sources=data.get("sources", [])
            )
        except requests.exceptions.Timeout:
            logger.error("API request timed out.")
            return QueryResponse(
                question=query,
                answer="⚠️ The server request timed out. The agent task took longer than expected.",
                status="timeout",
                error_message="Request timed out."
            )
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            return QueryResponse(
                question=query,
                answer=f"⚠️ Failed to connect to backend server: {str(e)}",
                status="error",
                error_message=str(e)
            )

    def get_workflow_graph(self) -> Optional[bytes]:
        """
        Fetches the Mermaid workflow PNG image from the /graph endpoint.
        """
        try:
            response = self.session.get(f"{self.base_url}/graph", timeout=10)
            if response.status_code == 200 and response.headers.get("content-type") == "image/png":
                return response.content
            return None
        except Exception as e:
            logger.warning(f"Could not fetch workflow graph: {e}")
            return None
