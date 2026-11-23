from unittest.mock import patch, MagicMock
from agentverse.agents.research import ResearchAgent


@patch("agentverse.agents.research.get_llm_client")
def test_research_agent_analyze_requirements(mock_get_llm_client):
    mock_client = MagicMock()
    mock_get_llm_client.return_value = mock_client

    # Configure mock LLM response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content='[{"task_id": "task-1", "description": "Implement login"}]'))]
    mock_client.chat.completions.create.return_value = mock_response

    agent = ResearchAgent(
        name="ResearchAgent",
        description="Analyzes project requirements and user stories.",
        user_stories=["As a user, I want to log in."]
    )

    result = agent.analyze_requirements()
    assert isinstance(result, list)
    assert len(result) == 1
