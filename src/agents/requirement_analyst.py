from langchain_openai import ChatOpenAI
from models.requirement import RequirementAnalysis
from config import REQUIREMENT_ANALYST_PROMPT_VERSION
from prompts.registry import get_prompt

class RequirementAnalyst:
    def __init__(self):
        # Higher values of temperature like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. 
        # Temperature is set to 0 for maximum consistency.
        self.model = ChatOpenAI(model="gpt-5.5", temperature=0) 
        self.structured_model = self.model.with_structured_output(RequirementAnalysis)
        self.prompt_template = get_prompt("requirement_analyst", REQUIREMENT_ANALYST_PROMPT_VERSION)

    def analyze(self, requirement: str) -> RequirementAnalysis:
        prompt = self.prompt_template.format(requirement = requirement)
        result = self.structured_model.invoke(prompt)
        return result