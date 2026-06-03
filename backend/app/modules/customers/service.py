from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.modules.categories.repo import category_repo
from app.modules.categories.schema import CategoryCreate, CategoryUpdate

class CategoryService:
    
    def get_all_categories(self, db: Session):
        return category_repo.get_all_categories(db)        

    def get_category_by_id(self, db: Session, id: int):
        category= category_repo.get_category_by_id(db, id)
        if not category:
            raise HTTPException(
                status_code= 404,
                detail= "Category not found"
            )
        return category
        
    def create_category(self, db: Session, data: CategoryCreate):
        existing=  category_repo.get_category_by_name(db, data.name)
        if existing:raise HTTPException(
            status_code= 400,
            detail= "Category already exist"
        )
        return category_repo.create_category(db, data.dict())
        
    def update_category(self, db:Session, id:int, data: CategoryUpdate):
        category= category_repo.get_category_by_id(db,id)
        if not category:
            raise HTTPException(
                status_code= 404,
                detail= "Category not found!"
            )
        update_category= data.dict(exclude_unset= True)
        return category_repo.update_category(db, category, update_category) 
    
    def delete_category(self, db:Session,id:int):
        category= category_repo.get_category_by_id(db, id)
        if not category:
            raise HTTPException(
                status_code= 404,
                detail= "Category not found!"
            )
        return category_repo.delete_category(db, category)

category_service= CategoryService()
    
    
