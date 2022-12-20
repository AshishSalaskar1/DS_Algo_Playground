from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel

class BlogItem(BaseModel):
    title: str
    body: str
    published: Optional[bool]

app = FastAPI()


@app.get("/")
def root_path():
    return {"date": {"name":"ashish","age":22}}


# PATH PARAMETERS
@app.get("/blog/{id}")
def show_blog(id: int):
    return {"data":id}


@app.get("/blog/{id}/comments")
def show_comments(id):
    return {"data":id, "comments":[1,2]}


# QUERY PARAMETERS
# /blog?limit=10&published=True
@app.get("/blog")
def show_blog_query(limit: int=10,is_published: bool=True, sorted: Optional[str] = None):
    return {"data":f"{limit} blogs from the DB which were {is_published}"}

# Request Body -> You need a Pydantic Model
@app.post("/create")
def create_blog(create_data: BlogItem):
    return {'created': create_data}