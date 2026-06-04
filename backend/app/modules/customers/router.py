from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.dependencies import get_current_user
from app.modules.customers.schema import CustomerCreate,CustomerResponse,CustomerUpdate
from app.modules.customers.service import customer_service

router = APIRouter(prefix="/customers",tags=["customers"])

@router.get("/", response_model=list[CustomerResponse])
def get_all_customers(db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    return customer_service.get_all_customers(db)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer_by_id(customer_id: int,db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    return customer_service.get_customer_by_id(db, customer_id)


@router.post("/", response_model=CustomerResponse)
def create_customer(data: CustomerCreate,db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    return customer_service.create_customer(db, data)


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int,data: CustomerUpdate,db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    return customer_service.update_customer(db,customer_id,data)


@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db:Session=Depends(get_db), current_user=Depends(get_current_user)):
    return customer_service.delete_customer(db, customer_id)