from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.modules.products.repo import product_repo
from app.modules.products.schema import ProductCreate, ProductUpdate

class ProductService:

    def get_all_products(self, db:Session):
        return product_repo.get_all_products(db)
    
    def get_product_by_id(self, db:Session, id: int):
        product= product_repo.get_product_by_id(db, id)
        if not product:
            raise HTTPException(
                status_code= 404,
                detail= "Product not found!"
            )
        return product
    
    def get_low_stock_products(self, db:Session):
        return product_repo.get_low_stock_products(db)
    
    def create_product(self, db:Session, data: ProductCreate):
        existing= product_repo.get_product_by_sku(db, data.sku)
        if existing:
            raise HTTPException(
                status_code=400,
                detail="SKU already exists"  
            )
        return product_repo.create_product(db, data.dict())
        
    def update_product(self, db:Session, id: int,data: ProductUpdate):
        product= product_repo.get_product_by_id(db, id)
        if not product:
            raise HTTPException(
                status_code= 404,
                detail= "Product not found!"
            )
        update_data=  data.dict(exclude_unset=True)
        return product_repo.update_product(db, product, update_data)
    
    def delete_product(self, db:Session,id:int):
        product= product_repo.get_product_by_id(db, id)
        if not product:
            raise HTTPException(
                status_code= 404,
                detail= "Product not found!"
            )
        return product_repo.delete_product(db, product)
        
product_service = ProductService()