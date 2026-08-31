from fastapi import APIRouter
from app.api.v1.banks.router import router as banks_router
from app.api.v1.clock.router import router as clock_router

api_router = APIRouter()
api_router.include_router(banks_router)
api_router.include_router(clock_router)