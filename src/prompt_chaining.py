import json


class PromptChaining:
    def __init__(self, client):
        self.client = client

    def generate_response(self, prompt):
        """
        Generates a response using the Ollama API.
        """
        response = self.client.generate(model="mistral", prompt=prompt, format="json")
        return json.loads(response["response"])

    def intermediate_response(self, prompt):
        """
        Generates a response using the Ollama API.
        """
        response = self.client.generate(model="mistral", prompt=prompt)
        return response["response"]

    def view_response(self, prompt):
        """
        Views a response using the Ollama API, in a structured format.
        """
        response = self.generate_response(prompt)
        return json.dumps(response, indent=2)

    def execute(self, source, question):
        prompt_1 = f"""You are a helpful assistant. Your task is to help answer a question given a document. The first step is to extract quotes relevant to the question from the document, delimited by ####. Please output the list of quotes using <quotes></quotes>. Respond with "No relevant quotes found!" if no relevant quotes were found.

        ####
        {source}
        ####
        """

        prompt_2 = f"""QUESTION: {question}"""

        quotes = self.intermediate_response(prompt_1 + prompt_2)

        prompt_3 = f"""
        Given a set of relevant quotes (delimited by <quotes></quotes>) extracted from a document and the original document (delimited by ####), please compose an answer to the question. Ensure that the answer is accurate.

        ####
        {source}
        ####

        {quotes}

        Return a structured response in JSON format containing the probability of the yes/no response to the question and a measure of confidence between 0 and 1. Provide output in JSON format as follows: {{"answer":{{"yes": <probability of yes>, "no": <probabuility of no>}}, "confidence": ..., "explanation": ...}}
        """

        return self.view_response(prompt_3)
