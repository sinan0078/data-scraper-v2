
from fastapi import APIRouter

router = APIRouter()

@router.post('/reports/generate')
def generate_report():
    return {'status': 'report generated'}

@router.get('/reports')
def list_reports():
    return []
