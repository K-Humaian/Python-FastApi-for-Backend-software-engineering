from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Message" : "Hello , This is default API endpoint"}


@app.get("/items/{item_id}/{item_name}")
def read_items (item_id: int,  item_name : str, q: str = None):
    return {"item_id": item_id, "item_name": item_name, "q": q}