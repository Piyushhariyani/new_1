from pydantic import BaseModel


class Change(BaseModel):
    change_id: str
    service_name: str
    change_type: str
    status: str
    risk: str
    implemented_at: str
    implemented_by: str
    summary: str
    rollback_available: bool