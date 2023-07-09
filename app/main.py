# https://derlin.github.io/introduction-to-fastapi-and-celery/

from random import randint
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field
from fastapi import FastAPI, Query, Path, HTTPException


app = FastAPI()


class UserIn(BaseModel):
    name: Annotated[str, Field(example="my-username", min_length=3, regex="^[a-z-]+$")]
    password: Annotated[str, Field(example="secret", min_length=5)]


class UserOut(BaseModel):
    id: int = randint(1, 100)
    name: str
    creation_date: datetime = datetime.now()


# Query parameter
@app.get("/user", response_description="The `new` user")
def create_user_with_query(name: Annotated[str, Query(min_length=3)]) -> UserOut:
    """
    Creates a new user. *Supports `markdown`!*. This route was created
    using the following github documentation by @derlin.

    [Introduction to FastAPI and Celery](https://derlin.github.io/introduction-to-fastapi-and-celery/02-fastapi/)
    """
    return UserOut(name=name)


# Path parameter
@app.get("/user/{name}")
def create_user_with_path(name: Annotated[str, Path(min_length=3)]) -> UserOut:
    """
    A Typical path parameter
    """
    return UserOut(name=name)


# Body parameter
@app.post("/user")
def create_user_with_request_body(user: UserIn) -> UserOut:
    """
    POST type API endpoint that takes in the User in object
    """
    return UserOut(**user.dict())


# Exceptions in FastAPI
@app.get("/error")
def error():
    raise HTTPException(
        status_code=500, detail="Just throwing an internal server error for fun :D"
    )
