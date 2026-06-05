from sqlalchemy.orm import Session
from app.modules.sales.model import Sale
from app.modules.sales.sale_item_model import SaleItem
from app.modules.products.model import Product

class SaleRepo:
    def get_all_sales(self, db: Session):
        return db.query(Sale).all()
   
    def get_sale_by_id(self, db: Session, id: int):
        return db.query(Sale).filter(Sale.id == id).first()
    
    def create_sale(self, db: Session, sale_data: dict):
        sale= Sale(**sale_data)
        db.add(sale)
        db.commit()
        db.refresh(sale)
        return sale
    
    def create_sale_item(self, db: Session, item_data: dict):
        item= SaleItem(**item_data)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
 
    def update_stock(self, db: Session, product_id: int, quantity: int):
        product= db.query(Product).filter(Product.id == product_id).first()
        product.stock_quantity -= quantity
        db.commit()
        
    def delete_sale(self, db: Session, sale):
        db.delete(sale)
        db.commit()
        return "Sale deleted successfully"        
        
sale_repo = SaleRepo()