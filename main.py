import strawberry
import uvicorn
from fastapi import FastAPI

from config import async_db

from Graphql.query import Query
from Graphql.mutation import Mutation

from strawberry.fastapi import GraphQLRouter


def init_app():
    apps = FastAPI(
        title="test",
        description="Fast API",
        version="1.0.0"
    )

    # @apps.on_event("startup")
    # async def startup():
    #     async with async_db() as session:
    #         async with session.begin():
    #             await session.run_sync(SQLModel.metadata.create_all)
    #
    # @apps.on_event("shutdown")
    # async def shutdown():
    #     await async_db.close()

    @apps.get('/')
    def home():
        return "welcome home!"

    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema)

    apps.include_router(graphql_app, prefix="/graphql")

    return apps


app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)
