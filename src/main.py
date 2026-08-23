from dotenv import load_dotenv

load_dotenv()

from workflow.graph import graph

def main():
    requirement = input("Enter a software requirement: ")

    initial_state = {
        "original_requirement": requirement,
        "requirement": requirement, 
        "analysis": None, 
        "is_valid": False, 
        "validation_message": None,
        "clarification": [],
        "retry_count": 0
    }
    result = graph.invoke(initial_state)
    analysis = result["analysis"]

    print("\nSUMMARY")
    print(analysis.summary)

    print("\nACCEPTANCE CRITERIA")
    for item in analysis.acceptance_criteria:
        print(f"- {item}")

    print("\nQUESTIONS")
    for question in analysis.questions:
        print(f"- {question}")

    print("\nVALID")
    print(result["is_valid"])

if __name__ == "__main__":
    main()