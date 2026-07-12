
from fastapi import APIRouter

router = APIRouter()

@router.get('/integrations')
def integrations():
    return []
