from fastapi import FastAPI
from app.config import settings
from app.database import Base, engine

from app.api.v1.banks.router import router as banks_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(banks_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return { "status": "ok", "project": settings.PROJECT_NAME }