from pydantic import BaseModel, Field
from typing import Optional

class BanksBase(BaseModel):
    taxId: str = Field(name="tax_id", description="CNPJ da instituição")
    name: str = Field(name="name", description="Nome do banco")
    fantasyName: str = Field(name="fantasy_name", description="Nome fantasia da instituição")
    ispb: Optional[str] = Field(name="ispb", description="Identificador do Sistema de Pagamneto Brasileiro")
    compeCode: str = Field(name="compe_code", description="Código do Sistema de Compensação de Cheques e Outros Papeis")
    
class BanksCreate(BanksBase):
    pass

class BanksUpdate(BanksBase):
    taxId: Optional[str] = None
    name: Optional[str] = None
    fantasyName: Optional[str] = None
    ispb: Optional[str] = None
    compeCode: Optional[str] = None

class BanksResponse(BanksBase):
    id: int
    class Config:
        from_attributes = True