from unittest.mock import MagicMock, patch
import pytest

from agentverse.agents.manager import ManagerAgent
from agentverse.task import Task


@patch("agentverse.llm.get_llm_client")
def test_manager_agent_openai_interaction(mock_get_llm_client):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="Task processed successfully"))
    ]
    mock_client.chat.completions.create.return_value = mock_response
    mock_get_llm_client.return_value = mock_client

    manager = ManagerAgent(name="Manager", description="Project Manager")
    task = Task(task_id="1", description="Design system architecture")
    manager.assign_task(task, "DeveloperAgent")

    assert task.assigned_agent == "DeveloperAgent"
    assert task.status == "pending"


@patch("agentverse.llm.get_llm_client")
def test_manager_agent_orchestrate_task_uses_llm(mock_get_llm_client):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="Orchestration plan"))
    ]
    mock_client.chat.completions.create.return_value = mock_response
    mock_get_llm_client.return_value = mock_client

    manager = ManagerAgent(name="Manager", description="Project Manager")
    task1 = Task(task_id="1", description="Task 1")

    manager.orchestrate_task([task1])

    # Assert that the LLM was called
    mock_client.chat.completions.create.assert_called()
