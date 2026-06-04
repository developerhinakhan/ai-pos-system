from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CustomerCreate(BaseModel):
    name: str
    email: Optional[str]= None
    contact_no: Optional[str]= None
    address: Optional[str]= None
    
class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str]= None
    contact_no: Optional[str]= None
    address: Optional[str]= None
    
class CustomerResponse(BaseModel):
    id: int
    name: str
    email: Optional[str] = None      
    contact_no: Optional[str] = None 
    address: Optional[str] = None    
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]= None
    
    class Config:
        from_attributes= True
    
  
