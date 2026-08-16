from langchain_openai import ChatOpenAI
from models.requirement import RequirementAnalysis

class RequirementAnalyst:
    def __init__(self):
        # Higher values of temperature like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. 
        # Temperature is set to 0 for maximum consistency.
        self.model = ChatOpenAI(model="gpt-5.5", temperature=0) 
        self.structured_model = self.model.with_structured_output(RequirementAnalysis)

    def analyze(self, requirement: str) -> RequirementAnalysis:
        prompt = f"""
                    You are a software requirement analyst.
                    Analyze the following software requirement:
                    {requirement}
                    Your responsibilities are:
                    1. Summarize the requirement clearly.
                    2. Produce testable acceptance criteria.
                    3. Identify important missing information.
                    4. Ask questions where the requirement is ambiguous.
                    Do not invent business rules that were not given.
                """
        result = self.structured_model.invoke(prompt)
        return result