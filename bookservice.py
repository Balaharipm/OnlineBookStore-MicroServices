from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    price: float

books_db = {}

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]

@app.post("/books/")
async def create_book(book: Book):
    books_db[book.id] = book
    return book
