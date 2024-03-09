import json


class QuestionReformulator:
    def __init__(self, client):
        self.client = client

    def llm_query(self, prompt):
        """
        Generates a response using the Ollama API.
        """
        response = self.client.generate(model="mistral", prompt=prompt)
        return response["response"]

    def clarify_objective(self, question):
        prompt = f"What is the objective of this question: '{question}'?"
        objective = self.llm_query(prompt)
        return objective

    def identify_key_elements(self, question):
        prompt = f"Identify the key elements in this question: '{question}'"
        key_elements = self.llm_query(prompt)
        return key_elements.split(
            ", "
        )  # Assuming the model returns a comma-separated list

    def rephrase_question(self, question, key_elements):
        prompt = f"Rephrase the question to make it clearer and more specific, focusing on these key elements: {', '.join(key_elements)}. Original question: '{question}'"
        rephrased_question = self.llm_query(prompt)
        return rephrased_question

    def generate_questions(self, rephrased_question):
        prompt = f"Generate five different variations of this question that could provide deeper insights: '{rephrased_question}'"
        questions = self.llm_query(prompt)
        return questions.split(
            "\n"
        )  # Assuming the model returns questions separated by newlines

    def process_question(self, question):
        objective = self.clarify_objective(question)
        key_elements = self.identify_key_elements(question)
        rephrased_question = self.rephrase_question(question, key_elements)
        questions = self.generate_questions(rephrased_question)
        return questions

    def multi_response_analysis(self, responses, question):
        prompt = (
            "Responses from multiple format of the same question is given below.\n"
            "---------------------\n"
            f"{responses}\n"
            "---------------------\n"
            f"Given the multiple responses that are trying to answer the same question({question}) in different ways,"
            "generate the final response by understanding different responses.\n"
            """Return a structured response in JSON format containing the probability of the yes/no response to the question and a measure of confidence between 0 and 1. Provide output in JSON format as follows: {{"answer":{{"yes": <probability of yes>, "no": <probabuility of no>}}, "confidence": ..., "explanation": ...}}"""
        )
        response = self.client.generate(model="mistral", prompt=prompt, format="json")
        return json.loads(response["response"])
