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
            # Placeholder for actual analysis and task generation.
            for i, story in enumerate(self.user_stories):
                tasks.append(Task(task_id=f"analyze_story_{i+1}", description=f"Analyze user story: '{story}'"))
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
