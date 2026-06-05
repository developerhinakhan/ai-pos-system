# Import routers for all modules
from fastapi import FastAPI
from app.core.config import settings
from app.modules.auth.router import router as auth_router
from app.modules.products.router import router as product_router
from app.modules.categories.router import router as category_router
from app.modules.customers.router import router as customer_router
from app.modules.sales.router import router as sale_router




# Import all models to register them with SQLAlchemy
# This ensures relationships are resolved correctly at startup
from app.modules.users.model import User
from app.modules.categories.model import Category
from app.modules.products.model import Product
from app.modules.customers.model import Customer
from app.modules.sales.model import Sale
from app.modules.sales.sale_item_model import SaleItem


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0",
    description="AI Powered POS System"
)


# Register routers
app.include_router(auth_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(customer_router)
app.include_router(sale_router)

# Health check endpoint
@app.get("/")
def root():
    return {
        "app": settings.APP_NAME,
        "status": "running",
        "version": "1.0.0"
    }