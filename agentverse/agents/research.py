from agentverse.agents import Agent
from agentverse.message import Message
from typing import Optional

class ResearchAgent(Agent):
    """
    Research Agent: Analyzes project requirements and user stories.
    """
    def __init__(
        self,
        name: str,
        description: str,
        llm_client=None,
    ):
        super().__init__(name, description)
        self.llm_client = llm_client

    def handle_message(self, message: Message) -> None:
        """Receive and acknowledge incoming messages."""
        print(f"ResearchAgent {self.name} received message from {message.sender}: {message.content}")

    def run(self, *args, **kwargs) -> None:
        """Placeholder run method for the initial workflow."""
        pass
