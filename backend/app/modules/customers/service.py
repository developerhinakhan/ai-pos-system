from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.modules.customers.schema import CustomerCreate, CustomerUpdate
from app.modules.customers.repo import customer_repo

class CustomerService:
    
    def get_all_customers(self, db: Session):
        return customer_repo.get_all_customers(db)        

    def get_customer_by_id(self, db: Session, id: int):
        customer= customer_repo.get_customer_by_id(db, id)
        if not customer:
            raise HTTPException(
                status_code= 404,
                detail= "customer not found"
            )
        return customer
        
    def create_customer(self, db: Session, data: CustomerCreate):
        existing= customer_repo.get_customer_by_email(db, data.email)
        if existing:raise HTTPException(
            status_code= 400,
            detail= "customer already exist"
        )
        return customer_repo.create_customer(db, data.dict())
        
    def update_customer(self, db:Session, id:int, data: CustomerUpdate):
        customer= customer_repo.get_customer_by_id(db,id)
        if not customer:
            raise HTTPException(
                status_code= 404,
                detail= "customer not found!"
            )
        update_customer= data.dict(exclude_unset= True)
        return customer_repo.update_customer(db, customer, update_customer) 
    
    def delete_customer(self, db:Session,id:int):
        customer= customer_repo.get_customer_by_id(db, id)
        if not customer:
            raise HTTPException(
                status_code= 404,
                detail= "customer not found!"
            )
        return customer_repo.delete_customer(db, customer)

customer_service= CustomerService()
    
