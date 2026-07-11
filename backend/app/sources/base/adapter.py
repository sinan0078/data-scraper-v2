
from abc import ABC, abstractmethod

class SourceAdapter(ABC):
    @abstractmethod
    async def search(self, query: str):
        pass
