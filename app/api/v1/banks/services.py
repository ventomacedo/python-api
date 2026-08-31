from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import Update

from .models import BanksModel
from .schemas import BanksCreate, BanksUpdate

def get_all_banks(db: Session, skip: int = 0, limit: int = 100) -> List[BanksModel]:
    return db.query(BanksModel).offset(skip).limit(limit).all()

def find_bank(db: Session, tax_id: str) -> Optional[BanksModel]:
    return db.query(BanksModel).filter(BanksModel.taxId == tax_id).first()

def create_bank(db: Session, bank: BanksCreate) -> BanksModel:
    try:
        new_bank = BanksModel(**bank.model_dump())
        db.add(new_bank)
        db.commit()
        db.refresh(new_bank)
        return new_bank
    except Exception as error:
        print(error)

def update_bank(db: Session, id: int, bank: BanksUpdate) -> BanksModel:
    try:
        stmt = (Update(BanksModel).where(BanksModel.id == id).values(**bank).returning(BanksModel))
        updated_bank = db.scalar(stmt)
        db.commit()
        return updated_bank    
    except Exception as error:
        print(error)

def delete_bank(db: Session, id: int) -> BanksModel:
    try:
        bank = db.get(BanksModel, id)
        db.delete(bank)
        db.commit()
    except Exception as error:
        print(error)
    finally:
        return None