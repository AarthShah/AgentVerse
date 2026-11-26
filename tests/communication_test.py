import datetime
import unittest
from unittest.mock import MagicMock

from agentverse.agents import Agent
from agentverse.message import Message, TaskMessage, ResultMessage


class DummyAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name=name, description="Dummy agent for testing")
        self.received_messages = []

    def receive_message(self, message: Message) -> None:
        self.received_messages.append(message)


class TestAgentCommunication(unittest.TestCase):
    def test_message_creation(self):
        msg = Message(sender="AgentA", receiver="AgentB", content="Hello")
        self.assertEqual(msg.sender, "AgentA")
        self.assertEqual(msg.receiver, "AgentB")
        self.assertEqual(msg.content, "Hello")
        self.assertIsInstance(msg.timestamp, datetime.datetime)

    def test_task_message_creation(self):
        task_msg = TaskMessage(
            sender="Manager",
            receiver="Developer",
            content="Implement feature X",
            task_id="task-123"
        )
        self.assertEqual(task_msg.sender, "Manager")
        self.assertEqual(task_msg.receiver, "Developer")
        self.assertEqual(task_msg.content, "Implement feature X")
        self.assertEqual(task_msg.task_id, "task-123")
        self.assertIsInstance(task_msg.timestamp, datetime.datetime)

    def test_result_message_creation(self):
        result_msg = ResultMessage(
            sender="Developer",
            receiver="Manager",
            content="Feature implemented",
            task_id="task-123",
            success=True
        )
        self.assertEqual(result_msg.sender, "Developer")
        self.assertEqual(result_msg.receiver, "Manager")
        self.assertEqual(result_msg.content, "Feature implemented")
        self.assertEqual(result_msg.task_id, "task-123")
        self.assertTrue(result_msg.success)
        self.assertIsInstance(result_msg.timestamp, datetime.datetime)

    def test_agent_send_and_receive_message(self):
        agent_a = DummyAgent("AgentA")
        agent_b = DummyAgent("AgentB")

        msg = Message(sender="AgentA", receiver="AgentB", content="Test transmission")
        
        # Simulating send_message or direct delivery mechanism
        agent_b.receive_message(msg)

        self.assertEqual(len(agent_b.received_messages), 1)
        received = agent_b.received_messages[0]
        self.assertEqual(received.content, "Test transmission")
        self.assertEqual(received.sender, "AgentA")
        self.assertEqual(received.receiver, "AgentB")


if __name__ == "__main__":
    unittest.main()
