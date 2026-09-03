from sqlalchemy.orm import Session
from app.modules.customers.model import Customer

class CustomerRepo:
    def get_all_customers(self, db: Session):
        return db.query(Customer).filter(Customer.is_active == True).all()
    
    def get_customer_by_id(self, db: Session,id:int):
        return db.query(Customer).filter(Customer.id==id).first()
    
    def get_customer_by_email(self,db:Session, email:str):
        return db.query(Customer).filter(Customer.email==email).first()
    
    def create_customer(self, db: Session, customer_data: dict):
        customer= Customer(**customer_data)
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer
    
    def update_customer(self, db: Session, customer, update_data: dict):  
        for key, value in update_data.items():
            setattr(customer,key,value)
        db.commit()
        db.refresh(customer)
        return customer
        
    def delete_customer(self, db: Session, customer):
        customer.is_active = False
        db.commit()
        db.refresh(customer)
        return "Customer deactivated successfully"
    

customer_repo= CustomerRepo() 
