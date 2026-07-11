
class DocumentNormalizer:
    def normalize(self, doc: dict) -> dict:
        return {
            "source": doc.get("source"),
            "title": doc.get("title","").strip(),
            "content": doc.get("content","").strip(),
            "url": doc.get("url"),
            "metadata": doc.get("metadata", {})
        }
