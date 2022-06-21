from fastapi import FastAPI

from app.api.qraphql.router import graphql_router

app = FastAPI()
app.include_router(graphql_router, prefix="/graphql")


@app.get("/")
async def root():
    return {"message": "Hello World"}
