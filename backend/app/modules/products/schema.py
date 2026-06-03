from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    stock_quantity: int
    low_stock_alert: int
    category_id: int
    description: Optional[str]= None
    weight: Optional[float]= None
    image_url: Optional[str]= None
    
class ProductUpdate(BaseModel):
    name: Optional[str]= None
    sku: Optional[str]= None
    price: Optional[float]= None
    stock_quantity: Optional[int]= None
    low_stock_alert: Optional[int]= None
    category_id: Optional[int]= None
    description: Optional[str]= None
    weight: Optional[float]= None
    image_url: Optional[str]= None

class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    price: float
    stock_quantity: int
    low_stock_alert: int
    category_id: int
    description: Optional[str]= None
    weight: Optional[float]= None
    image_url: Optional[str]= None
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]= None
    class Config:
        from_attributes= True

