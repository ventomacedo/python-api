from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from .schemas import BanksCreate, BanksResponse
from .services import get_all_banks, create_bank, find_bank

router = APIRouter(prefix="/banks", tags=["Banks"])

@router.get("/", response_model=List[BanksResponse])
def get_banks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_banks(db=db, skip=skip, limit=limit)

@router.post("/", response_model=BanksResponse, status_code=status.HTTP_201_CREATED)
def post_banks(bank: BanksCreate, db: Session = Depends(get_db)):
    return create_bank(db=db, bank=bank)

@router.get("/{bank_cnpj}", response_model=BanksResponse)
def get_bank(bank_cnpj: int, db: Session = Depends(get_db)):
    bank = find_bank(db=db, bank_cnpj=bank_cnpj)
    if not bank:
        raise HTTPException(status_code=404, detail="Banco não encontrado.")
    return bank