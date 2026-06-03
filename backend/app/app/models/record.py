from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class RecordModel(BaseModel):
    record_id       : str      = Field(default_factory=generate_uuid)
    user_id         : str
    filename        : str      = ""
    scan_path       : str      = ""
    s3_scan_path    : str      = ""      # NEW
    heatmap_url     : str      = ""
    s3_heatmap_path : str      = ""
    s3_report_path  : str      = ""
    prediction      : str      = "Pending"
    confidence_score: float    = 0.0
    status          : str      = "Uploaded"
    created_at      : datetime = Field(default_factory=datetime.utcnow)

    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)
        return d