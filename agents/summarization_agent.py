# Summarization Agent: Generates marketing/product summaries


import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class SummarizationAgent:
	def __init__(self):
		api_key = os.getenv("GEMINI_API_KEY")
		genai.configure(api_key=api_key)
		self.model = genai.GenerativeModel("gemini-pro")

	def summarize(self, product_id: str, context: str = None):
		prompt = f"Generate a marketing description for product {product_id}."
		if context:
			prompt += f" Context: {context}"
		try:
			response = self.model.generate_content(prompt)
			return response.text
		except Exception as e:
			return f"[Gemini LLM Error] {e}"
