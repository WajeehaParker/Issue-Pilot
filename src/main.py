from dotenv import load_dotenv
from agents.requirement_analyst import RequirementAnalyst
load_dotenv()

def main():
    requirement = input("Enter a software requirement: ")
    analyst = RequirementAnalyst()
    result = analyst.analyze(requirement)
    print("\nSUMMARY")
    print(result.summary)
    print("\nACCEPTANCE CRITERIA")
    for item in result.acceptance_criteria:
        print(f"- {item}")
    print("\nQUESTIONS")
    for question in result.questions:
        print(f"- {question}")

if __name__ == "__main__":
    main()