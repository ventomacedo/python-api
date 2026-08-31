from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class BanksModel(Base):
    __tablename__ = "banks"

    id: Mapped[int] = mapped_column(name="id", primary_key=True, index=True, autoincrement=True)
    taxId: Mapped[str] = mapped_column(name="tax_id", nullable=False)
    name: Mapped[str] = mapped_column(name="name", nullable=False)
    fantasyName: Mapped[str] = mapped_column(name="fantasy_name", nullable=False)
    ispb: Mapped[str] = mapped_column(name="ispb", nullable=True)
    compeCode: Mapped[str] = mapped_column(name="compe_code", nullable=False)
