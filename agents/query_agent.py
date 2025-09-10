# Query Agent: Converts natural language to Cypher queries

class QueryAgent:
	def __init__(self, neo4j_driver):
		self.driver = neo4j_driver

	def question_to_cypher(self, question: str) -> str:
		# TODO: Integrate with LLM or rule-based mapping
		# For now, return a placeholder Cypher query
		return "MATCH (p:Product) RETURN p LIMIT 5"

	def run_query(self, cypher: str):
		with self.driver.session() as session:
			result = session.run(cypher)
			return [record.data() for record in result]
