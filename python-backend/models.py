from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: Optional[int] = None # ID will be assigned by the database
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "medium"
    due_date: Optional[datetime] = None
    recurring: Optional[bool] = False
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class TaskCreate(BaseModel): #For creation
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "medium"
    due_date: Optional[datetime] = None
    recurring: Optional[bool] = False

class TaskUpdate(BaseModel): #For edits
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None
    recurring: Optional[bool] = None
    updated_at: datetime = datetime.now()


# Example usage
if __name__ == "__main__":
    new_task = TaskCreate(
        title="Buy groceries",
        priority="high",
        due_date=datetime(2023, 10, 10),
        description="Complete the AI project by end of the week",
        recurring=True
    )
    print(new_task.model_dump())  # Outputs as Dict