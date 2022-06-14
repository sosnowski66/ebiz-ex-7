from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/dupa")
async def dupa():
    return {
        "msg": "dupa 123",
        "orm": "no orm"
    }


@app.post("/items")
async def create_item(item: Item):
    return item

