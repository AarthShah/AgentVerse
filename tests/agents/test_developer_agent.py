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

    def test_generate_code_exception_fallback(self):
        self.mock_llm_client.chat.completions.create.side_effect = Exception("API error")

        instruction = "Write a python script that prints Hello, World!"
        code = self.agent.generate_code(instruction)

        self.assertEqual(code, "# Placeholder code\npass")
        self.mock_llm_client.chat.completions.create.assert_called_once()


    def test_generate_code_exception_fallback_again(self):
        self.mock_llm_client.chat.completions.create.side_effect = Exception("Another error")

        instruction = "Write a python script that prints Hello, World!"
        code = self.agent.generate_code(instruction)

        self.assertEqual(code, "# Placeholder code\npass")
        self.mock_llm_client.chat.completions.create.assert_called_once()

    def test_generate_code_empty_instruction(self):
        self.mock_llm_client.chat.completions.create.return_value.choices[0].message.content = (
            "# Empty instruction handled\npass"
        )

        instruction = ""
        code = self.agent.generate_code(instruction)

        self.assertEqual(code, "# Empty instruction handled\npass")
        self.mock_llm_client.chat.completions.create.assert_called_once()

    def test_generate_code_none_instruction(self):
        self.mock_llm_client.chat.completions.create.side_effect = Exception("Invalid instruction")

        code = self.agent.generate_code(None)

        self.assertEqual(code, "# Placeholder code\npass")
        self.mock_llm_client.chat.completions.create.assert_called_once()


if __name__ == "__main__":
    unittest.main()
