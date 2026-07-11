
import hashlib

def document_hash(title: str, url: str) -> str:
    return hashlib.sha256(f"{title}{url}".encode()).hexdigest()
