from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.database import get_db
from app.modules.categories.schema import CategoryCreate, CategoryResponse, CategoryUpdate
from app.modules.categories.service import category_service
from app.core.dependencies import get_current_user
from app.core.cache import get_cache, set_cache, delete_cache

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryResponse])
def get_all_category(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # Check cache first
    cached = get_cache("categories:all")
    if cached:
        return cached

    # Not in cache → get from database
    categories = category_service.get_all_categories(db)

    # Save to cache for 10 minutes
    set_cache("categories:all", jsonable_encoder(categories), expire=600)

    return categories


@router.get("/{id}", response_model=CategoryResponse)
def get_category_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return category_service.get_category_by_id(db, id)


@router.post("/", response_model=CategoryResponse)
def create_category(
    data: CategoryCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    category = category_service.create_category(db, data)
    # Clear cache
    delete_cache("categories:all")
    return category


@router.put("/{id}", response_model=CategoryResponse)
def update_category(
    id: int,
    data: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    category = category_service.update_category(db, id, data)
    # Clear cache
    delete_cache("categories:all")
    return category


@router.delete("/{id}")
def delete_category(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    result = category_service.delete_category(db, id)
    # Clear cache
    delete_cache("categories:all")
    return result