from pydantic import BaseModel

class RequirementAnalysis(BaseModel):
    summary: str
    acceptance_criteria: list[str]
    questions: list[str]
    blocking_questions: list[str]
    is_requirement_clear: bool