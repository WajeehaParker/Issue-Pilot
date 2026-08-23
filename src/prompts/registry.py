from prompts.requirement_analyst import (REQUIREMENT_ANALYST_V1, REQUIREMENT_ANALYST_V2)

PROMPT_REGISTRY = {
    "requirement_analyst" : {
        "v1" : REQUIREMENT_ANALYST_V1,
        "v2" : REQUIREMENT_ANALYST_V2
    }
}

def get_prompt(prompt_name: str, version: str) -> str:
    if prompt_name not in PROMPT_REGISTRY:
        raise ValueError(f"Prompt '{prompt_name}' does not exist.")
    versions = PROMPT_REGISTRY[prompt_name]
    if version not in versions:
        raise ValueError(f"Version '{version}' does not exist for prompt '{prompt_name}'.")
    return versions[version]