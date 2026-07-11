
from pydantic import BaseModel
from datetime import datetime

class Document(BaseModel):
    source: str
    title: str
    content: str
    author: str | None = None
    url: str
    created_at: datetime
    metadata: dict = {}
