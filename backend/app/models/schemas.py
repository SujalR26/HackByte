from typing import Optional
from pydantic import BaseModel


class PresignRequest(BaseModel):
    filename: Optional[str] = None
    content_type: Optional[str] = None


class ClassifyRequest(BaseModel):
    photo_url: str
    lat: float
    lng: float
    reporter_name: Optional[str] = None


class ReportCreateRequest(BaseModel):
    photo_url: str
    lat: float
    lng: float
    hazard_type: Optional[str] = None
    severity: Optional[str] = None
    department: Optional[str] = None
    summary: Optional[str] = None
    complaint_letter: Optional[str] = None


class AdminBulkUpdateRequest(BaseModel):
    ids: list[str]
    status: str
