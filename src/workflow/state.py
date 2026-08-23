from typing import TypedDict
from models.requirement import RequirementAnalysis

class RequirementState(TypedDict):
    original_requirement: str
    requirement: str
    analysis: RequirementAnalysis | None
    is_valid: bool
    validation_message: str | None
    clarification: list[str]
    retry_count: int