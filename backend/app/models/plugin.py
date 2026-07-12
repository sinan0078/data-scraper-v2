
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Plugin(Base):
    __tablename__ = "plugins"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
