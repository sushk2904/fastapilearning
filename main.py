from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True #Would not throw error 422 that is unprocessable entity even if the field is empty by the client 
    rating: Optional[int] = None

my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p



@app.get("/") #The thing inside the quotation mark or the decorator inside refers to the path we have to access or go to
def read_root():
    return {"welcome to my api!!!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    
    my_posts.append(post_dict)
    return {"data": post_dict}

#if this method is stated below the /posts/{id} method it would throw an error because /post/latest and latest would be considered as the same variable as id and would throw out an error on it 
#so take care while defining the routes because two routes can mismatch accidentally

'''
@app.get("/posts/latest")
def get_latest_potest():
    post = my_posts[len(my_posts)-1]
    return {"the post is": post}
'''   


@app.get("/posts/{id}")
def get_post(id : int): # : int this automatically converts the id to int for us
    post = find_post(id) # We have to do it in int because when we use find_post method it returns us a string instead of an integer that is why we are converting it here using int() but later on we in the function itself put the strict parameter of accepting only int so we removed the int() from here
    return {"post_detail": post}




 

# title str, content str