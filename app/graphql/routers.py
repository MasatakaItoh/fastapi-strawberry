import strawberry

from app.graphql.resolvers import get_user, create_user
from app.graphql.schemas import UserPayload


@strawberry.type
class Query:
    user: UserPayload = strawberry.field(resolver=get_user)


@strawberry.type
class Mutation:
    user_create: UserPayload = strawberry.field(resolver=create_user)
