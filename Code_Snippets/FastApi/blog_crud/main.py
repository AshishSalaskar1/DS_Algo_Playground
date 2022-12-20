from typing import Union, Optional
from fastapi import FastAPI
from . import schemas, models
from .database import engine

# CREATE DB TABLES
models.Base.metadata.create_all(engine)


app = FastAPI()


@app.post("/blog")
def create_blog(request: schemas.BlogItem):
    return {'title': request.title, "body": request.body}