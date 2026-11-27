from abc import ABC, abstractmethod
from typing import List, Any
from agentverse.message import Message

class Agent(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.inbox: List[Message] = []

    def receive_message(self, message: Message) -> None:
        self.inbox.append(message)

    def process_inbox(self) -> None:
        while self.inbox:
            message = self.inbox.pop(0)
            self.handle_message(message)

    @abstractmethod
    def handle_message(self, message: Message) -> None:
        pass
