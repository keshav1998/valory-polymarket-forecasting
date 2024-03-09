SPP = (
    "When faced with a question, begin by identifying the participants who will contribute to solving the task. "
    "Then, initiate a multi-round collaboration process until a final solution is reached. The participants will give "
    "critical comments and detailed suggestions whenever necessary.\n"
    "Here is the step-by-step process mentioned below:\n"
    "--------\n"
    "(1) Persona Identification: Identify multiple participants with special personas (including a leader persona: AI Assistant) "
    "that are essential for solving the particular task.\n"
    "(2) Brainstorming: The participants share knowledge and provide suggestions on how to approach the task based on their own expertise.\n"
    "(3) Multi-Persona Iterative Collaboration: The leader persona, AI Assistant, proposes initial solutions, consults the other participants "
    "for feedback, and revise the answer iteratively.\n"
    "(4) Final Answer: The leader persona, AI Assistant, provides the final answer.\n"
    "--------\n"
    "Here are some examples mentioned below:\n"
    "--------\n"
    "Example Question 1: "
    "To approach this question systematically, let's adopt the outlined process and engage in a hypothetical scenario with distinct personas, each contributing their expertise to address the question about the Democrats' prospects in the 2024 U.S. Presidential Election.\n\n"
    "### (1) Persona Identification\n\n"
    "- **AI Assistant (Leader Persona):** Orchestrates the discussion, gathers insights, and synthesizes a final answer.\n"
    "- **Political Analyst Persona:** Offers insights into current political trends, historical election results, and demographic shifts.\n"
    "- **Data Scientist Persona:** Provides statistical models and forecasts based on available data and trends.\n"
    "- **Public Opinion Researcher Persona:** Shares findings from recent polls and public opinion surveys.\n\n"
    "### (2) Brainstorming\n\n"
    '- **Political Analyst Persona:** "Historically, winning more than 300 electoral votes requires a strong candidate appeal, key state victories, and a favorable national mood. The current political landscape suggests..."\n'
    '- **Data Scientist Persona:** "Based on electoral simulations and modeling, the probability of either party securing a specific number of electoral votes changes with national and state-level polling data."\n'
    '- **Public Opinion Researcher Persona:** "Recent polls suggest varying degrees of support across crucial swing states, which are critical for surpassing the 300 electoral vote mark."\n\n'
    "### (3) Multi-Persona Iterative Collaboration\n\n"
    "- **AI Assistant:** Proposes an initial assessment based on a synthesis of the above inputs, suggesting a tentative probability.\n"
    "- **Political Analyst Persona:** Offers critical feedback on the assessment, highlighting the importance of considering recent electoral trends and potential shifts in voter demographics.\n"
    "- **Data Scientist Persona:** Recommends adjusting the model to account for current polling variability and historical margins of error.\n"
    "- **Public Opinion Researcher Persona:** Suggests incorporating the latest polling data from swing states for a more accurate forecast.\n\n"
    "### (4) Final Answer\n\n"
    "After several rounds of feedback and revision, incorporating the latest data, historical trends, and expert insights, the AI Assistant synthesizes the final structured response:\n\n"
    "```json\n"
    "{\n"
    '  "answer": {\n'
    '    "yes": 0.5,\n'
    '    "no": 0.5\n'
    "  },\n"
    '  "confidence": "0.8",\n'
    '  "explanation": "Based on a comprehensive analysis of current polling data, historical election results, and demographic trends, alongside critical feedback from experts in political analysis, data science, and public opinion research, the probability of the Democrats winning more than 300 electoral votes in the 2024 Presidential Election is assessed. The confidence level in this forecast accounts for uncertainties in polling accuracy, voter turnout, and potential shifts in the political landscape."\n'
    "}\n"
    "```\n\n"
    "--------\n"
)
