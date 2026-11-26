from typing import List, Any

class Message:
    def __init__(self, sender: str, content: Any):
        self.sender = sender
        self.content = content

class TaskMessage(Message):
    def __init__(self, sender: str, task_id: str, content: Any):
        super().__init__(sender, content)
        self.task_id = task_id

class ResultMessage(Message):
    def __init__(self, sender: str, task_id: str, result: Any):
        super().__init__(sender, result)
        self.task_id = task_id
        self.result = result
