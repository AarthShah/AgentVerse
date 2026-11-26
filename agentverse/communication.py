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

class TaskMessage(Message):
    """
    Represents a message with an assigned task.

    Attributes:
        sender (str): The name of the agent sending the message.
        recipient (str): The name of the agent receiving the message.
        content (str): The content of the message (usually task details).
        task_description (str): A detailed description of the task.
        due_date (datetime.date): The due date for the task.
    """
    def __init__(self, sender: str, recipient: str, content: str, task_description: str, due_date: datetime.date):
        super().__init__(sender, recipient, content)
        self.task_description = task_description
        self.due_date = due_date

    def __repr__(self) -> str:
        return f"TaskMessage(sender='{self.sender}', recipient='{self.recipient}', content='{self.content}', task_description='{self.task_description}', due_date='{self.due_date}', timestamp='{self.timestamp}')"

class ResultMessage(Message):
    """
    Represents a message conveying the result or status update of an operation.

    Attributes:
        sender (str): The name of the agent sending the message.
        recipient (str): The name of the agent receiving the message.
        content (str): The content of the message.
        result_data (Any): The data or payload resulting from the operation.
        status (str): The outcome status of the operation (e.g., 'success', 'failure').
    """
    def __init__(self, sender: str, recipient: str, content: str, result_data: any, status: str):
        super().__init__(sender, recipient, content)
        self.result_data = result_data
        self.status = status

    def __repr__(self) -> str:
        return f"ResultMessage(sender='{self.sender}', recipient='{self.recipient}', content='{self.content}', result_data='{self.result_data}', status='{self.status}', timestamp='{self.timestamp}')"
