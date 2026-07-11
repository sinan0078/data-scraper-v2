
class SummarizerService:
    def summarize(self, text: str) -> str:
        return f"Summary: {text[:200]}"
