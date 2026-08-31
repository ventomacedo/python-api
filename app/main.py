from fastapi import FastAPI
from app.config import settings
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import api_router



Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(api_router, prefix="/api/v1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return { "status": "ok", "project": settings.PROJECT_NAME }