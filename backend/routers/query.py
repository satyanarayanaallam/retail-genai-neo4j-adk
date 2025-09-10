
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents.query_agent import QueryAgent
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
query_agent = QueryAgent(driver)

router = APIRouter()

class QueryRequest(BaseModel):
    question: str


@router.post("/query")
def query_endpoint(request: QueryRequest):
    cypher = query_agent.question_to_cypher(request.question)
    try:
        results = query_agent.run_query(cypher)
        return {"cypher": cypher, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
