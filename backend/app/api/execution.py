
from fastapi import APIRouter
router = APIRouter()

@router.get('/execution/workflows')
def workflows():
    return []
