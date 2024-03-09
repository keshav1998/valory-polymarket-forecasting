from src.prompts import SPP
import json


class SPPPrompting:
    def __init__(self, client):
        self.client = client

    def generate_response(self, query_str, context_str):
        """
        Generates a response using the Ollama API.
        """
        question_prompt = (
            "Context information from multiple sources is below.\n"
            "---------------------\n"
            f"{context_str}\n"
            "---------------------\n"
            "Given the process, example and context information, "
            "answer the query.\n"
            f"Query: {query_str}\n"
            "Answer: "
            'The response should be in JSON format in the following format: {"answer":{{"yes": <probability of yes>, "no": <probabuility of no>}}, "confidence": <confidence level between 0 and 1>, "explanation": ...}'
        )

        prompt = SPP + question_prompt
        response = self.client.generate(model="mistral", prompt=prompt, format="json")
        return json.loads(response["response"])
