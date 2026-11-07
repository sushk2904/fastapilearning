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




@app.get("/") #The thing inside the quotation mark or the decorator inside refers to the path we have to access or go to
def read_root():
    return {"welcome to my api!!!!"}

@app.get("/posts")
def get_posts():
    return {"this is your posts"}


@app.post("/createposts")
def create_posts(new_post: Post):
    
    
    print(new_post.dict())
    return {"data": new_post}

# title str, content str