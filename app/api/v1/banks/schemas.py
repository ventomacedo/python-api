from pydantic import BaseModel, Field
from typing import Optional

class BanksBase(BaseModel):
    cnpj: str = Field(description="CNPJ da instituição")
    name: str = Field(description="Nome do banco")
    fantasy_name: str = Field(description="Nome fantasia da instituição")
    ispb: Optional[str] = Field(description="Identificador do Sistema de Pagamneto Brasileiro")
    compe_code: str = Field(description="Código do Sistema de Compensação de Cheques e Outros Papeis")
    
class BanksCreate(BanksBase):
    pass

class BanksResponse(BanksBase):
    id: int
    class Config:
        from_attributes = True