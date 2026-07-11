
from fastapi import APIRouter
router = APIRouter()

@router.post('/api-keys')
def create_api_key():
    return {'status': 'created'}
