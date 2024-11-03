from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    project_id: int

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    project_id: int
