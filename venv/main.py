from fastapi import FastAPI
app =  FastAPI()

@app.get("/")
def read_root():
    return{"message:" "Hello, FastApi"}

@app.get("/items/{item_id}")
def read_root(item_id: int, q: str = None):
    return{"item_id": item_id, "Query": q}


