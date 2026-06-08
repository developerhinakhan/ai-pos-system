from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.modules.ai.service import ai_service
from app.core.dependencies import get_current_user
from app.core.cache import get_cache, set_cache, delete_cache

router = APIRouter(prefix="/ai", tags=["AI"])


@router.get("/low-stock")
def get_low_stock_analysis(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # Cache AI responses for 30 minutes
    cached = get_cache("ai:low-stock")
    if cached:
        return cached

    result = ai_service.get_low_stock_analysis(db)
    set_cache("ai:low-stock", result, expire=1800)
    return result


@router.get("/sales-insights")
def get_sales_insights(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    cached = get_cache("ai:sales-insights")
    if cached:
        return cached

    result = ai_service.get_sales_insights(db)
    set_cache("ai:sales-insights", result, expire=1800)
    return result


@router.get("/recommendations")
def get_recommendations(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    cached = get_cache("ai:recommendations")
    if cached:
        return cached

    result = ai_service.get_recommendations(db)
    set_cache("ai:recommendations", result, expire=1800)
    return result