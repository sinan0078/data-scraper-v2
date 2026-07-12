
from fastapi import APIRouter

router = APIRouter()

@router.get('/admin/audit')
def audit_logs():
    return []
