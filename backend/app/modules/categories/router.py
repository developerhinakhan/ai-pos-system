from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.modules.categories.schema import CategoryCreate,CategoryResponse,CategoryUpdate
from app.modules.categories.service import category_service
from app.core.dependencies import get_current_user

router= APIRouter(prefix= "/categories", tags= ["Categories"])

@router.get("/", response_model= list[CategoryResponse])
def get_all_category(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return category_service.get_all_categories(db)

@router.get("/{id}",response_model=CategoryResponse)
def get_category_by_id(id:int, db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return category_service.get_category_by_id(db, id)

@router.post("/",response_model= CategoryResponse)
def create_category(data:CategoryCreate,db:Session=Depends(get_db), current_user = Depends(get_current_user)):
    return category_service.create_category(db,data)

@router.put("/{id}",response_model= CategoryResponse)
def update_category(id:int,data:CategoryUpdate,db:Session=Depends(get_db), current_user = Depends(get_current_user)):
    return category_service.update_category(db,id,data)

@router.delete("/{id}",response_model= CategoryResponse)
def delete_category(id:int,db:Session=Depends(get_db), current_user = Depends(get_current_user)):
    return category_service.delete_category(db,id)
