from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1,"title": "Title One", "author":"Author One", "category":"Category One"},
    {"id":2,"title": "Title Two", "author":"Author Two", "category":"Category Two"},
    {"id":3,"title": "Title Three", "author":"Author Three", "category":"Category Three"},
    {"id":4,"title": "Title Four", "author":"Author Four", "category":"Category Four"}
]

def getBook(i:int):
    for k, b in enumerate(books):
        if b["id"] == i:
            return b
    return -1

## CRUD ## ## ## ## HTTP requests

## Create           POST
## Read             GET
## Update           PUT or PATCH
## Delete           DELETE 

## Order matters with HTTP requests

## GET request
@app.get("/books")
async def read():
    return books

## Enhanced GET request with dynamic paramter
@app.get("/books/{param}")
async def read(param:str):
    required_book = getBook(int(param))
    if required_book == -1:
        return {"Message" : "The required book is not available"}
    return required_book