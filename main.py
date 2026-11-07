from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True #Would not throw error 422 that is unprocessable entity even if the field is empty by the client 
    rating: Optional[int] = None

my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "I like pizza", "id": 2}]


@app.get("/") #The thing inside the quotation mark or the decorator inside refers to the path we have to access or go to
def read_root():
    return {"welcome to my api!!!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    
    my_posts.append(post.dict())
    return {"data": post}

# title str, content str