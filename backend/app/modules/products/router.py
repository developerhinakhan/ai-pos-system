from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.database import get_db
from app.modules.products.schema import ProductCreate, ProductResponse, ProductUpdate
from app.modules.products.service import product_service
from app.core.dependencies import get_current_user
from app.core.cache import get_cache, set_cache, delete_cache

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[ProductResponse])
def get_all_products(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # Check cache first
    cached = get_cache("products:all")
    if cached:
        return cached

    # Not in cache → get from database
    products = product_service.get_all_products(db)

    # Save to cache for 5 minutes
    set_cache("products:all", jsonable_encoder(products))

    return products


@router.get("/low-stock", response_model=list[ProductResponse])
def get_low_stock_products(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return product_service.get_low_stock_products(db)


@router.get("/{id}", response_model=ProductResponse)
def get_product_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return product_service.get_product_by_id(db, id)


@router.post("/", response_model=ProductResponse)
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    product = product_service.create_product(db, data)
    # Clear cache so next GET gets fresh data
    delete_cache("products:all")
    return product


@router.put("/{id}", response_model=ProductResponse)
def update_product(
    id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    product = product_service.update_product(db, id, data)
    # Clear cache
    delete_cache("products:all")
    return product


@router.delete("/{id}")
def delete_product(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    result = product_service.delete_product(db, id)
    # Clear cache
    delete_cache("products:all")
    return result