from sqlalchemy.orm import Session
from app.modules.categories.model import Category

class CategoryRepo:
    def get_all_categories(self, db: Session):
        return db.query(Category).all()

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
        db.delete(category)
        db.commit()
        return "Category Deleted Succesfully"

category_repo = CategoryRepo()