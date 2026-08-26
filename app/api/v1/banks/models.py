from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class BanksModel(Base):
    __tablename__ = "banks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    cnpj: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    fantasy_name: Mapped[str] = mapped_column(nullable=False)
    ispb: Mapped[str] = mapped_column(nullable=True)
    compe_code: Mapped[str] = mapped_column(nullable=False)
