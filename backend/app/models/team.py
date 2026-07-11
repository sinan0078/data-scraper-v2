
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Team(Base):
    __tablename__ = 'teams'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
