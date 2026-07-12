
from fastapi import APIRouter

router = APIRouter()

@router.get('/enterprise-ai/status')
def status():
    return {"status": "operational"}
