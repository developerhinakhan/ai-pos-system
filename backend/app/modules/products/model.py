from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    sku = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    low_stock_alert = Column(Integer, default=10)
    weight = Column(Float, nullable=True)
    image_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    category = relationship("Category", back_populates="products")
    sale_items = relationship("SaleItem", back_populates="product")