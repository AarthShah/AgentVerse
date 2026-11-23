from openai import OpenAI
from agentverse.config import get_openai_api_key

RESEARCH_ANALYSIS_PROMPT_TEMPLATE = (
    "Analyze the following project requirements and user stories. "
    "Break them down into distinct, structured tasks suitable for a software development team. "
    "Ensure each task has a clear title, description, and expected outcome.\n\n"
    "Requirements & User Stories:\n{content}"
)

def get_llm_client() -> OpenAI:
    """Returns an initialized OpenAI client."""
    api_key = get_openai_api_key()
    return OpenAI(api_key=api_key)


def test_connection() -> bool:
    """Tests the connection to the OpenAI API."""
    client = get_llm_client()
    try:
        client.models.list()
        return True
    except Exception:
        return False
