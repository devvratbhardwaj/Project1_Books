from fastapi import FastAPI

app = FastAPI()

books = [
    {"id":1,"title": "Title One", "author":"One", "category":"Category One"},
    {"id":2,"title": "Title Two", "author":"Two", "category":"Category Two"},
    {"id":3,"title": "Title Three", "author":"Three", "category":"Category Three"},
    {"id":4,"title": "Title Four", "author":"Four", "category":"Category Four"}
]

## Practice overloading

def findBook_by_id(x:int):       
    ## index, element       
    for i, e in enumerate(books):
        if e["id"] == x:
            return e
    return -1

def findBook_by_category(x:str):
    for i, e in enumerate(books):
        if e["category"] == x:
            return e
    return -1


## CRUD ## ## ## ## HTTP requests
## Create           POST
## Read             GET
## Update           PUT or PATCH
## Delete           DELETE 


# Order matters with APIs

# As FastAPI looks for all the functions in
# a chronological order from top to bottom.

# Therefore, we need to keep APIs with static 
# parameters above APIs with dynamic parameters.

## GET request
@app.get("/books")
async def read():
    return books

# ## Enhanced GET request with dynamic paramter
@app.get("/books/{param}")
async def get_book_by_id(param:int):    
    ## FastAPI actually puts use to annotations (Is the decorator responsible for this? OR Is this Pydantic?)
    ## param in this case must be an int
    required_book = findBook_by_id(param)
    if required_book == -1:
        return {"Message" : "The required book is not available"}
    return required_book

#**** To put a space in an API URL, we use %20

@app.get("/books/by_category/{category}")
async def get_book_by_category(category:str):
    ## FastAPI actually puts use to annotations (Is the decorator responsible for this? OR Is this Pydantic?)
    ## Category in this case must be a string
    # category = " ".join(category.split("%"))
    required_book = findBook_by_category(category)
    if required_book == -1:
        return {"Message" : "The required book is not available"}
    return required_book

@app.get("/books/")
async def get_book_by_author_query(author:str):
    for book in books:
        if book['author'].casefold() == author.casefold():
            return book
    return {"Message":"Book doesn't exist"}