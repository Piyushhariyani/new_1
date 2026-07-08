from __future__ import annotations


def validate_service_name(service_name: str) -> str:
    """
    Validate a service name.
    """

    if not service_name or not service_name.strip():
        raise ValueError("Service name cannot be empty.")

    return service_name.strip()


def validate_ticket_id(ticket_id: str) -> str:
    """
    Validate ticket id.
    """

    if not ticket_id or not ticket_id.strip():
        raise ValueError("Ticket ID cannot be empty.")

    return ticket_id.strip()


def validate_change_id(change_id: str) -> str:
    """
    Validate change id.
    """

    if not change_id or not change_id.strip():
        raise ValueError("Change ID cannot be empty.")

    return change_id.strip()