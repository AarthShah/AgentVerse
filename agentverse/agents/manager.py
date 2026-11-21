from typing import List
from agentverse.agents import Agent
from agentverse.task import Task


class ManagerAgent(Agent):
    """Manages task orchestration and agent assignment within AgentVerse."""

    def __init__(self, name: str, description: str, managed_agents: List[str] = None):
        super().__init__(name, description)
        self.managed_agents = managed_agents or []

    def assign_task(self, task: Task, agent_name: str) -> None:
        """Assign a task to a specific agent."""
        task.assigned_agent = agent_name
        task.status = "assigned"

    def orchestrate_task(self, tasks: List[Task]) -> None:
        """Orchestrate a list of tasks and assign them to available agents."""
        for task in tasks:
            if task.status == "pending" and self.managed_agents:
                # Simple round-robin or first available agent assignment logic for now
                assigned_agent = self.managed_agents[0]
                self.assign_task(task, assigned_agent)
                print(f"Orchestrated task {task.task_id} and assigned to {assigned_agent}")

    def run(self, *args, **kwargs):
        """Run the manager agent's primary loop."""
        pass
