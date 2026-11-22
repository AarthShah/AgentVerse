"""Configuration for AgentVerse."""

import os

# OpenAI API settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4")

# Default settings
DEFAULT_MAX_ITERATIONS = 10
DEFAULT_TEMPERATURE = 0.7
