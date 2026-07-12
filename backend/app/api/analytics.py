
from fastapi import APIRouter

router = APIRouter()

@router.get('/analytics/trends')
def trends():
    return {"trends": []}
