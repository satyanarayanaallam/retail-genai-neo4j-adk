
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents.summarization_agent import SummarizationAgent

summarization_agent = SummarizationAgent()

router = APIRouter()

class SummarizationRequest(BaseModel):
    product_id: str
    context: str = None  # e.g., marketing or personalization context


@router.post("/summarize")
def summarization_endpoint(request: SummarizationRequest):
    try:
        summary = summarization_agent.summarize(request.product_id, request.context)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
