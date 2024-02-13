from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/items/{item_id}')

def read_item(item_id: int):
    return{'item_id': item_id}

@app.get('/items/')


def get_items_info(skip: int = 0, limit: int = 5, q:str = None):
    if q:
        return {"skip": skip, 'limit':limit, 'q':q}
    else:
        {'skip':skip, 'limit': limit}
        
@app.get('/users/{user_id}')

def read_user(user_id):
    return{'user_id': user_id}

@app.get('/users/{user_id}/items/')
def read_user(user_id, skip, limit):
    return{"user_id": user_id, "skip":skip, "limit": limit}