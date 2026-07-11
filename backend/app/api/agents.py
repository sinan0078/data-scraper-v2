
from fastapi import APIRouter

router = APIRouter()

@router.post('/agents/research')
async def research():
    return {"status": "started"}
