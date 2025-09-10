
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents.recommendation_agent import RecommendationAgent
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
recommendation_agent = RecommendationAgent(driver)

router = APIRouter()

class RecommendationRequest(BaseModel):
    customer_id: str
    context: str = None  # e.g., product/category or scenario


@router.post("/recommendation")
def recommendation_endpoint(request: RecommendationRequest):
    try:
        recommendations = recommendation_agent.recommend(request.customer_id, request.context)
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
