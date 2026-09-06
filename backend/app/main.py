from fastapi import FastAPI

from app.core.config import settings
from app.core.supabase import supabase


app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API for the Krushi Mitra agro-tourism platform",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Krushi Mitra Agro Tech API",
        "status": "running",
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "supabase": "configured",
    }