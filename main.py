from agentverse.agents.manager import ManagerAgent
from agentverse.task import Task

def main():
    print("AgentVerse is starting...")

    # Instantiate the ManagerAgent
    manager = ManagerAgent(name="Manager", description="Manages task orchestration and agent assignment.")

    # Create sample tasks
    task1 = Task(task_id="1", description="Develop user authentication module.")
    task2 = Task(task_id="2", description="Implement API endpoints for data retrieval.")
    task3 = Task(task_id="3", description="Write unit tests for the authentication module.")
    task4 = Task(task_id="4", description="Set up CI/CD pipeline.")

    sample_tasks = [task1, task2, task3, task4]

    # Orchestrate the tasks and demonstrate LLM reasoning integration
    print("\nOrchestrating tasks...")
    manager.orchestrate_task(sample_tasks)

    print("\nExecuting sample task with LLM reasoning...")
    result = manager.run(task1)
    print(f"LLM-generated output for task '{task1.description}':")
    print(result)
    print("Task orchestration complete.")

if __name__ == "__main__":
    main()
