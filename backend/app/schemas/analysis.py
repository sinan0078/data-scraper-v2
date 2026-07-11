
from pydantic import BaseModel

class AnalysisResult(BaseModel):
    summary: str
    sentiment: dict
    keywords: list[str]
