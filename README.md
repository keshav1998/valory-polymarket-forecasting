# valory-polymarket-forecasting
Demonstrate proficiency in interacting with and fine-tuning Large Language Models (LLM).

## TASKS:

1. Prompt Engineering: Craft a series of prompts designed to test the model's capabilities in prediction tasks.
Examples of questions on which to make a prediction can be found at this prediction
market platform: https://polymarket.com/. The model should return a structured response
(e.g. json) containing the probability of the yes/no response to the question and a measure of confidence between 0 and 1.

2. Prompt Optimization: Develop different prompting approaches. This may include prompt chaining,
reformulating questions, or using specific keywords.

3. Fine-Tuning: Describe in detail (with references to scientific articles and technologies) how to fine-tune
a pre-trained LLM for prediction tasks.


## PROMPTING TECHNIQUES USED:
1. Prompt Chaining
2. Multipersona Prompting
3. Reformulating Question

## EXTRA MODULES REQUIRED:
1. Information retreival pipeline to provide context to the model behind the questions.
2. A Rag based approach where retreived information is temporarily indexed and a RAG pipeline is created around that for each specific question

## Reference:
1. https://arxiv.org/html/2402.18563v1#S4
2. https://arxiv.org/pdf/2307.05300.pdf
3. https://www.prompthub.us/blog/exploring-multi-persona-prompting-for-better-outputs
4. https://www.promptingguide.ai/techniques/cot
5. https://arxiv.org/html/2312.00949v2
6. https://bmjopen.bmj.com/content/bmjopen/8/11/e024996/DC2/embed/inline-supplementary-material-2.pdf
7. https://www.philschmid.de/fine-tune-llms-in-2024-with-trl
