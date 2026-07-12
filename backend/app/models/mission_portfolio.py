
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class MissionPortfolio(Base):
    __tablename__ = "mission_portfolios"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
