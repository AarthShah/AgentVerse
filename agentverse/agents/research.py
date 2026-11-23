from agentverse.agents import Agent
from agentverse.task import Task
from typing import List, Optional

class ResearchAgent(Agent):
    """
    Research Agent: Analyzes project requirements and user stories.
    """
    def __init__(
        self,
        name: str,
        description: str,
        llm_client=None,
        user_stories: Optional[List[str]] = None,
    ):
        super().__init__(name, description)
        self.llm_client = llm_client
        self.user_stories = user_stories if user_stories else []

    def add_user_story(self, user_story: str):
        """Adds a user story to the research agent's backlog."""
        self.user_stories.append(user_story)

    def analyze_requirements(self) -> List[Task]:
        """
        Analyzes the gathered user stories and generates initial tasks.
        This is a placeholder for the actual requirement analysis logic.
        """
        tasks = []
        if not self.user_stories:
            # If no user stories, create a placeholder task to gather them.
            tasks.append(Task(task_id="gather_requirements", description="Gather initial project requirements and user stories."))
        else:
            prompt = f"""
Analyze the following user stories and provide a structured output including:
1. Key Features: List the main functionalities derived from the stories.
2. Potential Ambiguities: Identify any unclear or contradictory statements.
3. Technical Considerations: Note any high-level technical aspects or dependencies.

User Stories:
{'\n'.join(self.user_stories)}

Structured Analysis:
"""
            # Assuming self.llm_client is an instance of a class that has a method to interact with an LLM
            # and returns a structured response. This part might need adjustment based on the actual LLM client implementation.
            # For now, we'll simulate a response.
            try:
                # Replace this with actual LLM call
                # llm_response = self.llm_client.generate(prompt)
                # Simulate LLM response for demonstration
                llm_response = {
                    "key_features": ["User authentication", "Data storage", "Reporting dashboard"],
                    "ambiguities": ["Specify authentication method (OAuth, JWT, etc.)", "Define data retention policy."],
                    "technical_considerations": ["Needs a database (e.g., PostgreSQL)", "API design for external integrations."]
                }

                # Generate tasks from LLM response
                tasks.append(Task(task_id="identify_key_features", description=f"Key Features: {', '.join(llm_response.get('key_features', []))}", status="analyzed"))
                tasks.append(Task(task_id="resolve_ambiguities", description=f"Potential Ambiguities: {', '.join(llm_response.get('ambiguities', []))}", status="pending"))
                tasks.append(Task(task_id="document_technical_considerations", description=f"Technical Considerations: {', '.join(llm_response.get('technical_considerations', []))}", status="documented"))

            except Exception as e:
                print(f"Error during requirement analysis: {e}")
                # Fallback to a simpler task if LLM fails
                tasks.append(Task(task_id="analyze_stories_fallback", description="Review user stories and identify core requirements."))
        return tasks

    def run(self, *args, **kwargs):
        """
        The main execution method for the Research Agent.
        Currently, it analyzes requirements if user stories are available.
        """
        if self.user_stories:
            print(f"Research Agent {self.name}: Analyzing requirements...")
            return self.analyze_requirements()
        else:
            print(f"Research Agent {self.name}: No user stories provided. Awaiting input.")
            # In a real scenario, this might involve waiting for input or initiating a process to get stories.
            return []
