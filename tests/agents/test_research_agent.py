from unittest.mock import patch, MagicMock
from agentverse.agents.research import ResearchAgent


@patch("agentverse.agents.research.get_llm_client")
def test_research_agent_analyze_requirements(mock_get_llm_client):
    mock_client = MagicMock()
    mock_get_llm_client.return_value = mock_client

    agent = ResearchAgent(
        name="ResearchAgent",
        description="Analyzes project requirements and user stories.",
        user_stories=["As a user, I want to log in."]
    )

    result = agent.analyze_requirements()
    assert isinstance(result, dict)
