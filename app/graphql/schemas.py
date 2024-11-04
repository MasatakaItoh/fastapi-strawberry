from typing import Optional, List

import strawberry

# Project


@strawberry.type
class Project:
    id: int
    name: str
    description: Optional[str] = None
    owner: Optional["User"] = None
    members: List["User"] = strawberry.field(default_factory=list)
    tasks: List["Task"] = strawberry.field(default_factory=list)


@strawberry.type
class ProjectPayload(Project):
    pass


@strawberry.input
class ProjectInput:
    id: str


@strawberry.input
class ProjectCreateInput:
    name: str
    description: Optional[str] = None
    owner_id: int


# Task


@strawberry.type
class Task:
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    project_id: int


# User


@strawberry.type
class User:
    id: int
    username: str
    owned_projects: List["Project"] = strawberry.field(default_factory=list)
    projects: List["Project"] = strawberry.field(default_factory=list)


@strawberry.type
class UserPayload(User):
    pass


@strawberry.input
class UserInput:
    id: str


@strawberry.input
class UserCreateInput:
    username: str
    password: str
