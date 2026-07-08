from pydantic import BaseModel


class Service(BaseModel):
    service_name: str
    service_id: str
    status: str
    region: str
    error_rate_percent: float
    average_latency_ms: int
    cpu_usage_percent: int
    memory_usage_percent: int
    last_checked: str
    active_incident_ids: list[str]