
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class AnalysisResultDB(Base):
    __tablename__ = "analysis_results"
    id: Mapped[int] = mapped_column(primary_key=True)
    summary: Mapped[str]
