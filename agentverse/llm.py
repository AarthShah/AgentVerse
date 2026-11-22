from openai import OpenAI
from agentverse.config import get_openai_api_key

def get_llm_client() -> OpenAI:
    """Returns an initialized OpenAI client."""
    api_key = get_openai_api_key()
    return OpenAI(api_key=api_key)
