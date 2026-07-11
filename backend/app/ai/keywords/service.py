
class KeywordService:
    def extract(self, text: str) -> list[str]:
        words = text.split()
        return list(set(words[:10]))
