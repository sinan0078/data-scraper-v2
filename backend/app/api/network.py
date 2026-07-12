
from fastapi import APIRouter

router = APIRouter()

@router.get('/network/graph')
def graph():
    return {"status": "ready"}
