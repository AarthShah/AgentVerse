from typing import List
from agentverse.agents import Agent
from agentverse.task import Task
from agentverse.llm import get_llm_client


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
        client = get_llm_client()
        for task in tasks:
            if task.status == "pending" and self.managed_agents:
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "You are a helpful manager agent."},
                            {"role": "user", "content": f"Decide how to handle task: {task.description}"}
                        ]
                    )
                    reasoning = response.choices[0].message.content
                    print(f"Manager reasoning for task {task.task_id}: {reasoning}")
                except Exception as e:
                    print(f"LLM call failed: {e}")

                # Simple round-robin or first available agent assignment logic for now
                assigned_agent = self.managed_agents[0]
                self.assign_task(task, assigned_agent)
                print(f"Orchestrated task {task.task_id} and assigned to {assigned_agent}")

    def process_inbox(self) -> None:
        """Iterate through the agent's inbox, process messages, and clear the inbox."""
        if not hasattr(self, "inbox") or not self.inbox:
            return
        
        for message in self.inbox:
            # Process message based on type or content
            print(f"ManagerAgent {self.name} processing message from {message.sender}: {message.content}")
        
        self.inbox.clear()

    def run(self, *args, **kwargs):
        """Run the manager agent's primary loop."""
        pass
