
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Trend(Base):
    __tablename__ = "trends"
    id: Mapped[int] = mapped_column(primary_key=True)
    keyword: Mapped[str]
