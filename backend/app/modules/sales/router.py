from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.modules.sales.schema import SaleCreate,SaleResponse,SaleItemResponse,SaleItemCreate
from app.modules.sales.service import sale_service
from app.core.dependencies import get_current_user

router= APIRouter(prefix= "/sales", tags= ["Sales"])

@router.get("/", response_model= list[SaleResponse])
def get_all_sales(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return sale_service.get_all_sales(db)

@router.get("/{id}",response_model=SaleResponse)
def get_sale_by_id(id:int, db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return sale_service.get_sale_by_id(db, id)

@router.post("/", response_model=SaleResponse)
def create_sale(data: SaleCreate,db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return sale_service.create_sale(db, data, current_user.id)

@router.delete("/{id}")
def delete_sale(id:int,db:Session=Depends(get_db), current_user = Depends(get_current_user)):
    return sale_service.delete_sale(db,id)
