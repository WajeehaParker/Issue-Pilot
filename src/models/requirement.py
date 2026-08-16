from pydantic import BaseModel

class RequirementAnalysis(BaseModel):
    summary: str
    acceptance_criteria: list[str]
    questions: list[str]