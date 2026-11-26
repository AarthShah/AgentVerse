from abc import ABC, abstractmethod
from agentverse.agents.research import ResearchAgent
from agentverse.agents.developer import DeveloperAgent
from agentverse.agents.testing import TestingAgent
from agentverse.agents.security import SecurityAgent
from agentverse.message import Message, TaskMessage, ResultMessage

__all__ = ["Agent", "ResearchAgent", "DeveloperAgent", "TestingAgent", "SecurityAgent", "Message", "TaskMessage", "ResultMessage"]

class Agent(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.inbox: list = []

    def receive_message(self, message: Message) -> None:
        """Receive an incoming message and append it to the inbox."""
        self.inbox.append(message)

    def send_message(self, recipient: 'Agent', message: Message) -> None:
        """Send a message to a recipient agent."""
        print(f"From: {self.name} | To: {recipient.name} | Content: {message.content}")
        if hasattr(recipient, "receive_message"):
            recipient.receive_message(message)

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
