
from fastapi import APIRouter

router = APIRouter()

@router.get('/intelligence/briefing')
def briefing():
    return {"status": "ready"}
