from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import List
from datetime import datetime

app = FastAPI()

class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"

class OrderItem(BaseModel):
    book_id: int
    quantity: int

class Order(BaseModel):
    id: int
    customer_id: int
    items: List[OrderItem]
    status: OrderStatus
    created_at: datetime

orders_db = {}

@app.post("/orders/")
async def create_order(order: Order):
    orders_db[order.id] = order
    return order

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_db[order_id]
