from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Welcome to the Home Page"}

@app.get("/search")
def search(
    q: Annotated[str, Query(min_length=1)]
):
    return {"you_searched_for": q}


@app.get("/products")
def get_products(
    q: Annotated[str, Query(min_length=1)],
    category: str = "all",
    max_price: float = 1000
):
    return{
        "Search": q,
        "Category": category,
        "Max Price": max_price
    }