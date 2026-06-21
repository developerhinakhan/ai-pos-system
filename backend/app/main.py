# Import routers for all modules
from fastapi import FastAPI
from app.core.config import settings
from app.modules.auth.router import router as auth_router
from app.modules.products.router import router as product_router
from app.modules.categories.router import router as category_router
from app.modules.customers.router import router as customer_router
from app.modules.sales.router import router as sale_router
from app.modules.ai.router import router as ai_router
from fastapi.responses import RedirectResponse




# Import all models to register them with SQLAlchemy
# This ensures relationships are resolved correctly at startup
from app.modules.users.model import User
from app.modules.categories.model import Category
from app.modules.products.model import Product
from app.modules.customers.model import Customer
from app.modules.sales.model import Sale
from app.modules.sales.sale_item_model import SaleItem
from app.database import Base, engine

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0",
    description="AI Powered POS System"
)

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(auth_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(customer_router)
app.include_router(sale_router)
app.include_router(ai_router)

# Health check endpoint
@app.get("/health", include_in_schema=False)
def health_check():
    return {
        "app": settings.APP_NAME,
        "status": "running",
        "version": "1.0.0"
    }

# Root redirects to docs
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")
    
