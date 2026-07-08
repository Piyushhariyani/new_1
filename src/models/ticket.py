from pydantic import BaseModel


class Ticket(BaseModel):
    ticket_id: str
    service_name: str
    priority: str
    status: str
    subject: str
    description: str
    created_at: str
    customer_impact: str
    assigned_group: str