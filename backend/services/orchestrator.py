from agents.query_agent import QueryAgent
from agents.recommendation_agent import RecommendationAgent
from agents.summarization_agent import SummarizationAgent
from backend.services.tools import run_cypher_query, summarize_product, recommend_products

# Example orchestrator for handling user queries

def handle_user_query(question, neo4j_driver):
    query_agent = QueryAgent(None, neo4j_driver)
    cypher = query_agent.question_to_cypher(question)
    results = run_cypher_query(neo4j_driver, cypher)
    return results

def handle_recommendation(customer_id, context, neo4j_driver):
    return recommend_products(neo4j_driver, customer_id, context)

def handle_summarization(product_id, context, genai_client=None):
    return summarize_product(product_id, context)
