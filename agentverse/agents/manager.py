from typing import List, Dict, Any
from agentverse.agents import Agent
from agentverse.task import Task
from agentverse.llm import get_llm_client
from agentverse.message import Message

class ManagerAgent(Agent):
    """Manages task orchestration and agent assignment within AgentVerse."""

    def __init__(self, name: str, description: str, managed_agents: List[str] = None, **kwargs):
        super().__init__(name, description, **kwargs)
        self.managed_agents = managed_agents or []
        self.inbox: List[Message] = []
        self.task_queue: List[Task] = []
        self.llm_client = get_llm_client() # Initialize LLM client here

    def assign_task(self, task: Task, agent_name: str) -> None:
        """Assign a task to a specific agent."""
        task.assigned_agent = agent_name
        task.status = "assigned"
        # In a real scenario, this would involve sending a message to the agent
        print(f"Assigning task {task.task_id} to {agent_name}")

    def orchestrate_task(self) -> None:
        """Orchestrate a list of tasks and assign them to available agents."""
        
        # Define the initial task for the DeveloperAgent
        initial_task = Task(
            task_id="T0",
            description="Generate a simple 'Hello World' Python application.",
            status="pending",
            dependencies=[]
        )
        self.task_queue.append(initial_task)

        # Process tasks from the queue
        while self.task_queue:
            task = self.task_queue.pop(0) # Get the next task
            if task.status == "pending" and self.managed_agents:
                # For this simple case, directly assign to the first managed agent (DeveloperAgent)
                # In a more complex scenario, this would involve LLM-based decision making
                assigned_agent = self.managed_agents[0] 
                self.assign_task(task, assigned_agent)
                print(f"Task {task.task_id} description: {task.description} assigned to {assigned_agent}")
            elif task.status == "completed":
                print(f"Task {task.task_id} is already completed.")
            else:
                print(f"Task {task.task_id} could not be assigned. Managed agents: {self.managed_agents}")


    def process_inbox(self) -> None:
        """Iterate through the agent's inbox, process messages, and clear the inbox."""
        if not self.inbox:
            return
        
        for message in self.inbox:
            # Process message based on type or content
            print(f"ManagerAgent {self.name} processing message from {message.sender}: {message.content}")
            # Example: If a task completion message is received, update task status
            if message.content.startswith("Task completed:"):
                task_id = message.content.split(":")[1].strip()
                for task in self.task_queue: # Check task_queue for pending tasks
                    if task.task_id == task_id:
                        task.status = "completed"
                        print(f"Manager received completion for task {task_id}")
                        break
                # Also check tasks that have already been assigned
                # This would require a different structure to track assigned tasks if they are not in task_queue
        
        self.inbox.clear()

    def run(self, *args, **kwargs):
        """Run the manager agent's primary loop."""
        print(f"ManagerAgent {self.name} starting its run loop.")
        # Initial orchestration to set up the first task
        self.orchestrate_task()
        # Process incoming messages (such as ResultMessage containing generated code)
        self.process_inbox()
        print(f"ManagerAgent {self.name} finished its initial run.")
