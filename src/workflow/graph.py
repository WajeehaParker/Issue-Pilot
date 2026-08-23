from langgraph.graph import StateGraph, START, END
from agents.requirement_analyst import RequirementAnalyst
from workflow.state import RequirementState

analyst = RequirementAnalyst()
MAX_RETRIES = 2

def analyze_requirement(state: RequirementState):
    requirement = state["requirement"]
    analysis = analyst.analyze(requirement)
    return {"analysis": analysis}

def validate_requirement(state: RequirementState):
    analysis = state["analysis"]
    if analysis is None:
        return {"is_valid": False, "validation_message": "No analysis was generated."}
    if not analysis.summary.strip():
        return {"is_valid": False, "validation_message": "The analysis has no summary."}
    if len(analysis.acceptance_criteria) == 0:
        return {"is_valid": False, "validation_message": "No acceptance criteria were generated."}
    if (not analysis.is_requirement_clear or len(analysis.blocking_questions) > 0):
        return {"is_valid": False, "validation_message": "The original requirement is not clear enough."}
    return {"is_valid": True, "validation_message": None}

def route_after_validation(state: RequirementState):
    if state["is_valid"]:
        return END
    if state["retry_count"] >= MAX_RETRIES:
        return "max_retries_reached"
    return "handle_missing_information"

def handle_missing_information(state: RequirementState):
    analysis = state["analysis"]
    print("\nThe requirement needs more information.")
    if state["validation_message"]:
        print(f"Reason: {state['validation_message']}")
    if analysis and analysis.blocking_questions:
        print("\nThe following information is required:")
        for question in analysis.blocking_questions:
            print(f"- {question}")
    if analysis and analysis.questions:
        print("\nQUESTIONS")
        for question in analysis.questions:
            print(f"- {question}")
            return {}

def collect_clarification(state: RequirementState):
    clarification = input("\nProvide additional information: ")
    state["clarification"] + [clarification]
    return {"clarification": clarification}

def update_requirement(state: RequirementState):
    original_requirement = state["requirement"]
    clarification = state["clarification"]
    clarification_text = "\n".join(f"- {item}" for item in clarification)
    updated_requirement = f"""
                            Original requirement:{original_requirement}
                            Additional clarification:{clarification_text}
                          """
    return {"requirement": updated_requirement, "retry_count": state["retry_count"] + 1}

def max_retries_reached(state: RequirementState):
    print("\nThe requirement is still not clear enough after multiple attempts.")
    print("The workflow will stop instead of continuing indefinitely.")
    return {}

workflow = StateGraph(RequirementState)

workflow.add_node("analyze_requirement", analyze_requirement)
workflow.add_node("validate_requirement", validate_requirement)
workflow.add_node("handle_missing_information", handle_missing_information)
workflow.add_node("collect_clarification", collect_clarification)
workflow.add_node("update_requirement", update_requirement)
workflow.add_node("max_retries_reached", max_retries_reached)

workflow.add_edge(START, "analyze_requirement")
workflow.add_edge("analyze_requirement", "validate_requirement")
workflow.add_conditional_edges("validate_requirement", route_after_validation)
workflow.add_edge("handle_missing_information", "collect_clarification")
workflow.add_edge("collect_clarification", "update_requirement")
workflow.add_edge("update_requirement", "analyze_requirement")
workflow.add_edge("max_retries_reached", END)

graph = workflow.compile()