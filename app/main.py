import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.database import SessionLocal
from app.graphql.routers import Query, Mutation


async def get_context():
    return {"db": SessionLocal()}


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, context_getter=get_context)
app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")
