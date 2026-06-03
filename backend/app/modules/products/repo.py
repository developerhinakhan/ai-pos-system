from sqlalchemy.orm import Session
from app.modules.products.model import Product

class ProductRepo:
    def get_all_products(self,db: Session):
        return  db.query(Product).all()
        
    def get_product_by_id(self, db: Session, id: int):  
        return db.query(Product).filter(Product.id==id).first()
    
    def get_low_stock_products(self, db: Session):
        return db.query(Product).filter(Product.stock_quantity <= Product.low_stock_alert).all()
        
    def create_product(self, db: Session, product_data: dict):
        product= Product(**product_data)
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
    
    def get_product_by_sku(self, db: Session, sku: str):
        return db.query(Product).filter(Product.sku == sku).first()

    def update_product(self, db: Session, product, update_data: dict):
        for key, value in update_data.items():
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
        return product
        
    def delete_product(self, db: Session, product):
        db.delete(product)
        db.commit()
        return "Product Deleted Succesfully✅"
    
product_repo= ProductRepo