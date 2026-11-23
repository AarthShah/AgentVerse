from abc import ABC, abstractmethod
from agentverse.agents.research import ResearchAgent

class Agent(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, *args, **kwargs):
        pass
