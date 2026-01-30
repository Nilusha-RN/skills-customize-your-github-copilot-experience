"""
FastAPI REST API Starter Code
Build a REST API for managing items with CRUD operations.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

# TODO: Import necessary modules if adding more features

# Initialize FastAPI app
app = FastAPI(
    title="Item Management API",
    description="A simple API for managing items",
    version="1.0.0"
)

# Pydantic model for validation
class ItemBase(BaseModel):
    """Base model for item data"""
    name: str
    description: Optional[str] = None
    price: float

class ItemCreate(ItemBase):
    """Model for creating a new item"""
    pass

class ItemUpdate(BaseModel):
    """Model for updating an item"""
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

class Item(ItemBase):
    """Complete item model with ID"""
    id: int

# In-memory storage for items (replace with a database later)
items_db: dict = {}
next_item_id: int = 1

# Endpoints

@app.get("/", tags=["Root"])
def root():
    """Welcome endpoint"""
    return {"message": "Welcome to Item Management API"}

# TODO: Implement GET /items endpoint to retrieve all items

# TODO: Implement GET /items/{item_id} endpoint to retrieve a single item

# TODO: Implement POST /items endpoint to create a new item

# TODO: Implement PUT /items/{item_id} endpoint to update an item

# TODO: Implement DELETE /items/{item_id} endpoint to delete an item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
