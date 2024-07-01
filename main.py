from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    body: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "title post 1", "content": "content post 1", "id": 1},
    {"title": "favorite foods", "content": "i like pizza", "id": 2},
]


@app.get("/")
async def root():
    return {"Message": "I am Rick"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.post("/posts")
async def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
