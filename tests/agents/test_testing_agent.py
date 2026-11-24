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
