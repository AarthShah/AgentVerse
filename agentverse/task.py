from typing import Optional


class Task:
    """Represents a unit of work to be performed within AgentVerse."""

    def __init__(
        self,
        task_id: str,
        description: str,
        status: str = "pending",
        assigned_agent: Optional[str] = None,
    ):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.assigned_agent = assigned_agent

    def __repr__(self) -> str:
        return (
            f"Task(task_id={self.task_id!r}, description={self.description!r}, "
            f"status={self.status!r}, assigned_agent={self.assigned_agent!r})"
        )
