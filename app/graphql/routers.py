import strawberry

from app.graphql.resolvers import get_user, create_user, get_project, create_project
from app.graphql.schemas import UserPayload, ProjectPayload


@strawberry.type
class Query:
    user: UserPayload = strawberry.field(resolver=get_user)
    project: ProjectPayload = strawberry.field(resolver=get_project)


@strawberry.type
class Mutation:
    createUser: UserPayload = strawberry.field(resolver=create_user)
    createProject: ProjectPayload = strawberry.field(resolver=create_project)
