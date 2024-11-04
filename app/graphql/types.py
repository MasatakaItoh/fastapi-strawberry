from typing import Optional, List

import strawberry
from pydantic import BaseModel

# Project


class Project(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner: Optional["User"] = None
    members: List["User"] = strawberry.field(default_factory=list)
    tasks: List["Task"] = strawberry.field(default_factory=list)

    class Config:
        orm_mode = True


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None


# Task


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


# User


class User(BaseModel):
    id: int
    username: str
    owned_projects: List["Project"] = strawberry.field(default_factory=list)
    projects: List["Project"] = strawberry.field(default_factory=list)

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    password: str
