import unittest
from unittest.mock import MagicMock, patch

from agentverse.agents.testing import TestingAgent


class TestTestingAgent(unittest.TestCase):
    def test__init__(self):
        # Mock the LLM client
        mock_llm_client = MagicMock()

        # Initialize the TestingAgent
        agent = TestingAgent(llm_client=mock_llm_client)

        # Assert that the agent was initialized correctly
        self.assertEqual(agent.name, "TestingAgent")
        self.assertEqual(agent.description, "Generates test cases for code.")
        self.assertIs(agent.llm_client, mock_llm_client)

    def test_generate_test_cases(self):
        mock_llm_client = MagicMock()
        mock_response = MagicMock()
        mock_response.content = "def test_foo(): pass"
        mock_llm_client.invoke.return_value = mock_response

        agent = TestingAgent(llm_client=mock_llm_client)
        code = "def foo(): return 42"
        result = agent.generate_test_cases(code)

        self.assertEqual(result, ["def test_foo(): pass"])
        mock_llm_client.invoke.assert_called_once()

    def test_generate_multiple_test_cases(self):
        mock_llm_client = MagicMock()
        mock_response = MagicMock()
        mock_response.content = "def test_foo(): pass\ndef test_bar(): pass"
        mock_llm_client.invoke.return_value = mock_response

        agent = TestingAgent(llm_client=mock_llm_client)
        code = "def foo(): return 42\ndef bar(): return 0"
        result = agent.generate_test_cases(code)

        self.assertEqual(result, ["def test_foo(): pass", "def test_bar(): pass"])
        mock_llm_client.invoke.assert_called_once()
