from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()


@app.get("/") #The thing inside the quotation mark or the decorator inside refers to the path we have to access or go to
def read_root():
    return {"welcome to my api!!!!"}

@app.get("/posts")
def get_posts():
    return {"this is your posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"message": f"title {payload['title']} content {payload['content']}"}
    