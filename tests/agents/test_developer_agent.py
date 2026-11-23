import unittest
from unittest.mock import MagicMock
from agentverse.agents.developer import DeveloperAgent


class TestDeveloperAgent(unittest.TestCase):
    def setUp(self):
        self.mock_llm_client = MagicMock()
        self.agent = DeveloperAgent(
            name="Developer",
            description="A developer agent",
            llm_client=self.mock_llm_client
        )

    def test_generate_code(self):
        self.mock_llm_client.chat.completions.create.return_value.choices[0].message.content = (
            "print('Hello, World!')"
        )

        instruction = "Write a python script that prints Hello, World!"
        code = self.agent.generate_code(instruction)

        self.assertEqual(code, "print('Hello, World!')")
        self.mock_llm_client.chat.completions.create.assert_called_once()


if __name__ == "__main__":
    unittest.main()
