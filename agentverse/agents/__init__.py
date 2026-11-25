from abc import ABC, abstractmethod
from agentverse.agents.research import ResearchAgent
from agentverse.agents.developer import DeveloperAgent
from agentverse.agents.testing import TestingAgent
from agentverse.agents.security import SecurityAgent

__all__ = ["ResearchAgent", "DeveloperAgent", "TestingAgent", "SecurityAgent"]

class Agent(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
