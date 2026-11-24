from abc import ABC, abstractmethod
from agentverse.agents.research import ResearchAgent
from agentverse.agents.developer import DeveloperAgent
from agentverse.agents.testing import TestingAgent

__all__ = ["ResearchAgent", "DeveloperAgent", "TestingAgent"]

class Agent(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
