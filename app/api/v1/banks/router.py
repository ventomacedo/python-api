from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from .schemas import BanksCreate, BanksResponse, BanksUpdate
from .services import get_all_banks, create_bank, update_bank, delete_bank, find_bank

router = APIRouter(prefix="/banks", tags=["Banks"])

@router.get("/", response_model=List[BanksResponse])
def get_banks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_banks(db=db, skip=skip, limit=limit)

@router.post("/", response_model=BanksResponse, status_code=status.HTTP_201_CREATED)
def post_banks(bank: BanksCreate, db: Session = Depends(get_db)):
    return create_bank(db=db, bank=bank)

@router.put("/{id}", response_model=BanksResponse, status_code=status.HTTP_200_OK)
def put_banks(id: int, bank: BanksUpdate, db: Session = Depends(get_db)):
    if not bank:
        raise HTTPException(status_code=400, detail="Nenhum campo válido foi enviado")
    
    dumped = bank.model_dump(exclude_unset=True)
    return update_bank(db=db, id=id, bank=dumped)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_banks(id: int, db: Session = Depends(get_db)):
    if not id:
        raise HTTPException(status_code=400, detail="Id é obrigatório")
    
    delete_bank(db=db, id=id)

@router.get("/{tax_id}", response_model=BanksResponse)
def get_bank(tax_id: str, db: Session = Depends(get_db)):
    bank = find_bank(db=db, tax_id=tax_id)
    if not bank:
        raise HTTPException(status_code=404, detail="Banco não encontrado.")
    return bank