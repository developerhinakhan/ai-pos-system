from fastapi import FastAPI
from app.core.config import settings
from app.modules.auth.router import router as auth_router

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version="1.0.0",
    description="AI Powered POS System"
)

# Register routers
app.include_router(auth_router)


# Health check endpoint
@app.get("/")
def root():
    return {
        "app": settings.APP_NAME,
        "status": "running",
        "version": "1.0.0"
    }