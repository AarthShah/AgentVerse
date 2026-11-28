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


def test_manager_agent_initialization():
    manager = ManagerAgent(name="ProjectManager", description="Coordinates tasks")
    assert manager.name == "ProjectManager"
    assert manager.description == "Coordinates tasks"


def test_manager_agent_send_task_message():
    manager = ManagerAgent(name="Manager", description="Project Manager")
    task = Task(task_id="101", description="Implement feature")
    message = manager.send_task_message(task, recipient="DeveloperAgent")

    assert message is not None
    assert message.recipient == "DeveloperAgent"
    assert message.content == task


def test_manager_agent_process_result_message():
    manager = ManagerAgent(name="Manager", description="Project Manager")
    task = Task(task_id="101", description="Implement feature", status="pending")
    result_msg = MagicMock()
    result_msg.task_id = "101"
    result_msg.status = "completed"
    result_msg.content = "Feature implemented successfully"

    manager.process_result_message(task, result_msg)

    assert task.status == "completed"
