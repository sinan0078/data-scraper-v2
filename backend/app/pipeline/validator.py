
class DocumentValidator:
    def validate(self, doc: dict) -> bool:
        required = ["source", "title", "content", "url"]
        return all(doc.get(k) for k in required)
