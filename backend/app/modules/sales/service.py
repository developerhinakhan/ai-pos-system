from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.modules.sales.repo import sale_repo
from app.modules.sales.schema import SaleCreate
from app.modules.products.repo import product_repo

class SaleService:



    def get_all_sales(self, db: Session):
        return sale_repo.get_all_sales(db)



    def get_sale_by_id(self, db: Session, id: int):
        sale= sale_repo.get_sale_by_id(db,id)
        if not sale:
            raise HTTPException(
                status_code= 404,
                detail= "Sale not found!"
            )
        return sale



    def create_sale(self, db: Session, data: SaleCreate, user_id: int):
        total= 0
        
        for item in data.items:
            total += item.quantity * item.unit_price
        final= total - (data.discount or 0) + (data.tax or 0)
        sale_data={
            "customer_id": data.customer_id,
            "user_id": user_id,
            "total_amount": total,
            "discount": data.discount or 0,
            "tax": data.tax or 0,
            "final_amount": final,
            "payment_method": data.payment_method,
            "status": "completed"
        }
        sale= sale_repo.create_sale(db, sale_data)
 
        
        for item in data.items:
            item_data={
                "sale_id": sale.id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "unit_price": item.unit_price,
                "total_price": item.quantity * item.unit_price
            }
            sale_repo.create_sale_item(db, item_data)
            sale_repo.update_stock(db, item.product_id, item.quantity)
        return sale


    def delete_sale(self, db: Session, id: int):
        sale = sale_repo.get_sale_by_id(db, id)  
        if not sale:
            raise HTTPException(
                status_code=404,
                detail="Sale not found"
            )
        return sale_repo.delete_sale(db, sale)  


sale_service = SaleService()