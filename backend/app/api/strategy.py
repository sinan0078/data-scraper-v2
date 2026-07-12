
from fastapi import APIRouter

router = APIRouter()

@router.get('/strategy/recommendations')
def recommendations():
    return {"recommendations": []}
