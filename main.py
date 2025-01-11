from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get("/blog")
def index(limit=25, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blog lists in db"}
    else:
        return {"data": f"{limit} blog list in db"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {"1", "2"}}


# @app.post('/blog')
# def create_blog():
#     return {'data':"Blog is created"}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def docreate_blog(request: Blog):
    return {"data": f"Blog is created with title as {request.title}"}
