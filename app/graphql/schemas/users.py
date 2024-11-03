import strawberry

from app.graphql.schemas.projects import Project


@strawberry.type
class User:
    id: int
    username: str
    owned_projects: list[Project] = []
    projects: list[Project] = []
