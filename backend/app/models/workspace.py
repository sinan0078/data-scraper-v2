
from sqlalchemy.orm import Mapped, mapped_column
from app.models.user import Base

class Workspace(Base):
    __tablename__ = "workspaces"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    user_id: Mapped[int]
