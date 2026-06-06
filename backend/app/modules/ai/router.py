from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.modules.ai.service import ai_service
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/ai", tags=["AI"])

@router.get("/low-stock")
def get_low_stock_analysis(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return ai_service.get_low_stock_analysis(db)

@router.get("/sales-insights")
def get_sales_insights(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return ai_service.get_sales_insights(db)

@router.get("/recommendations")
def get_recommendations(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return ai_service.get_recommendations(db)