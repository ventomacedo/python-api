from typing import List, Optional
from sqlalchemy.orm import Session

from .models import BanksModel
from .schemas import BanksCreate

def get_all_banks(db: Session, skip: int = 0, limit: int = 100) -> List[BanksModel]:
    return db.query(BanksModel).offset(skip).limit(limit).all()

def find_bank(db: Session, bank_cnpj: int) -> Optional[BanksModel]:
    return db.query(BanksModel).filter(BanksModel.cnpj == bank_cnpj).first()

def create_bank(db: Session, bank: BanksCreate) -> BanksModel:
    new_bank = BanksModel(**bank.model_dump())
    db.add(new_bank)
    db.commit()
    db.refresh(new_bank)
    return new_bank