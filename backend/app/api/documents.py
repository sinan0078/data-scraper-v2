
from fastapi import APIRouter

router = APIRouter()

@router.get("/documents")
def list_documents():
    return []
