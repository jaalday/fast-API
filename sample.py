from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# ---------------------------------------------
@app.get("/items/{item_id}")

def get_item(item_id: int):
     return{item_id}
 
@app.get("/items/")

def get_items(skip: int=5, limit: int=3, q: str=None):
    if q: 
        return{"q":q, "Skip":skip, "limit": limit}
    else:
        return{skip, limit}
    
    
@app.get('/users/{user_id}/items/')

def get_users(user_id, skip, limit):
    return{user_id, skip, limit}





    