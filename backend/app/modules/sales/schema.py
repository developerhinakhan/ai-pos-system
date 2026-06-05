from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SaleItemCreate(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

class SaleCreate(BaseModel):
    customer_id: Optional[int] = None
    discount: Optional[float] = 0
    tax: Optional[float] = 0
    payment_method: str = "cash"
    items: List[SaleItemCreate]

class SaleItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float
    total_price: float

    class Config:
        from_attributes = True

class SaleResponse(BaseModel):
    id: int
    total_amount: float
    discount: float
    tax: float
    final_amount: float
    payment_method: str
    status: str
    customer_id: Optional[int] = None
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    items: List[SaleItemResponse] = []

    class Config:
        from_attributes = True