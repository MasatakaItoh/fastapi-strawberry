from typing import List

from pydantic import BaseModel

from app.graphql.types.projects import Project


class User(BaseModel):
    id: int
    username: str
    owned_projects: List[Project] = []
    projects: List[Project] = []

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    password: str
