from fastapi import APIRouter, Depends
from typing import Any

from app.core.auth import get_current_user, get_current_user_id
from app.models.schemas import ReportCreateRequest
from app.services.reports import create_report

router = APIRouter(prefix="/api", tags=["reports"])


@router.post("/reports")
def create_report_endpoint(
    payload: ReportCreateRequest,
    user: Any = Depends(get_current_user),
):
    user_id = get_current_user_id(user)
    report_payload = {
        "user_id": user_id,
        "photo_url": payload.photo_url,
        "lat": payload.lat,
        "lng": payload.lng,
        "hazard_type": payload.hazard_type,
        "severity": payload.severity,
        "department": payload.department,
        "summary": payload.summary,
        "complaint": payload.complaint_letter,
    }
    report = create_report(user_id, report_payload)
    return {"report": report}
