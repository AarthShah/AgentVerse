"""Configuration for AgentVerse."""

import os

# OpenAI API settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4")

# Default settings
DEFAULT_MAX_ITERATIONS = 10
DEFAULT_TEMPERATURE = 0.7

# Testing Agent settings
# TODO: Add specific configurations for the Testing Agent if needed in the future.

# Security Agent settings
security_agent_config = {
    "enabled": True,
    "scan_timeout": 30,
}


def get_openai_api_key() -> str:
    """Retrieve the OpenAI API key, raising a ValueError if not set."""
    api_key = os.getenv("OPENAI_API_KEY", OPENAI_API_KEY)
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set or is empty."
        )
    return api_key
