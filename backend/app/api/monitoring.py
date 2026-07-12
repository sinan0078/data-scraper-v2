
from fastapi import APIRouter

router = APIRouter()

@router.get('/monitoring/watchlists')
def watchlists():
    return []
