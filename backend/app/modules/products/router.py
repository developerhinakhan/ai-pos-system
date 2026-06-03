from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.modules.products.schema import ProductCreate,ProductResponse,ProductUpdate
from app.modules.products.service import product_service
from app.core.dependencies import get_current_user

router= APIRouter(prefix= "/products",tags= ["Products"])

@router.get("/", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return product_service.get_all_products(db)

@router.get("/low-stock", response_model=list[ProductResponse])
def get_low_stock_products(db:Session=Depends(get_db), current_user = Depends(get_current_user)):
    return product_service.get_low_stock_products(db)

@router.get("/{id}",response_model=ProductResponse)
def get_product_by_id(id:int,db:Session=Depends(get_db), current_user = Depends(get_current_user)):
    return product_service.get_product_by_id(db, id)

@router.post("/",response_model=ProductResponse)
def create_product(data:ProductCreate,db:Session=Depends(get_db), current_user = Depends(get_current_user)):
    return product_service.create_product(db,data)

@router.put("/{id}",response_model=ProductResponse)
def update_product(id:int,data:ProductUpdate,db:Session=Depends(get_db), current_user = Depends(get_current_user)):
    return product_service.update_product(db,id,data)

@router.delete("/{id}",response_model=ProductResponse)
def delete_product(id:int,db:Session=Depends(get_db), current_user = Depends(get_current_user)):
    return product_service.delete_product(db,id)