from sqlalchemy.orm import Session
from app.modules.categories.model import Category

class CategoryRepo:
    def get_all_categories(self, db: Session):
        return db.query(Category).filter(Category.is_active == True).all()

    def get_category_by_id(self, db: Session, id: int):
        return db.query(Category).filter(Category.id==id).first()
    
    def get_category_by_name(self, db: Session, name:str):
        return db.query(Category).filter(Category.name==name).first()
    
    def create_category(self, db: Session,category_data: dict):
        category= Category(**category_data)
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
    
    def update_category(self, db: Session,category,update_data: dict):
        for key, value in update_data.items():
            setattr(category,key,value)
        db.commit()
        db.refresh(category)
        return category
    
    def delete_category(self,db: Session, category):
        category.is_active = False
        db.commit()
        db.refresh(category)
        return "Category deactivated successfully"

category_repo = CategoryRepo()