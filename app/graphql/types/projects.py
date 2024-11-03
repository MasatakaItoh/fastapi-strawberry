from typing import Optional, List

from pydantic import BaseModel

from app.graphql.types.tasks import Task
from app.graphql.types.users import User


class Project(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner = Optional[User]
    members = List[User] = []
    tasks = List[Task] = []

    class Config:
        orm_mode = True


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
