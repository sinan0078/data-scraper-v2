
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class APIKey(Base):
    __tablename__ = 'api_keys'
    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str]
