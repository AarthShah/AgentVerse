from typing import Any, List, Optional
from openai import OpenAI
from langchain.prompts import PromptTemplate
from agentverse.agents import Agent
from agentverse.task import Task


class DeveloperAgentError(Exception):
    """Exception raised by DeveloperAgent for errors during code generation."""
    pass


class DeveloperAgent(Agent):
    """
    Developer Agent: Responsible for generating code based on structured tasks and requirements.
    """

    CODE_PROMPT = PromptTemplate(
        input_variables=["instruction"],
        template="Generate Python code based on the following instruction:\n\n{instruction}\n\nReturn only the Python code implementation.",
    )

    def __init__(
        self,
        name: str = "DeveloperAgent",
        description: str = "Generates code implementations based on tasks.",
        llm_client=None,
    ):
        super().__init__(name=name, description=description)
        self.llm_client = llm_client

    def _call_llm(self, prompt: str) -> str:
        if self.llm_client is None:
            return f"# Implementation stub\npass\n"
        
        try:
            return self.llm_client.generate(prompt)
        except Exception as e:
            raise DeveloperAgentError(f"LLM call failed: {e}") from e

    def generate_code(self, instruction: str) -> str:
        prompt = self.CODE_PROMPT.format(instruction=instruction)
        response = self._call_llm(prompt)
        return response.strip()

    def run(self, task: Task, *args, **kwargs) -> str:
        """
        Execute code generation for a given task.
        """
        return self.generate_code(task.description)
