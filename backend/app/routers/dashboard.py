from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.dashboard import DashboardResumo
from app.services.dashboard_service import obter_resumo_dashboard


router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/resumo", response_model=DashboardResumo)
def obter_resumo(db: Session = Depends(get_db)):
    return obter_resumo_dashboard(db)