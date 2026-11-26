import datetime

class Message:
    """
    Represents a message exchanged between agents.

    Attributes:
        sender (str): The name of the agent sending the message.
        recipient (str): The name of the agent receiving the message.
        content (str): The content of the message.
        timestamp (datetime.datetime): The time at which the message was sent.
    """
    def __init__(self, sender: str, recipient: str, content: str):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = datetime.datetime.now()

    def __repr__(self) -> str:
        return f"Message(sender='{self.sender}', recipient='{self.recipient}', content='{self.content}', timestamp='{self.timestamp}')"
