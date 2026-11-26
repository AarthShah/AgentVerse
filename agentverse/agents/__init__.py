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

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
