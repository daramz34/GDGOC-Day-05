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
