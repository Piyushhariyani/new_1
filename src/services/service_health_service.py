from __future__ import annotations

from src.config import SERVICE_HEALTH_FILE
from src.utils.json_loader import load_json


class ServiceHealthService:
    """Business logic for service health operations."""

    def __init__(self) -> None:
        self.data = load_json(SERVICE_HEALTH_FILE)

    def list_services(self) -> list[dict]:
        """Return all services."""

        return [
            {
                "service_name": service["service_name"],
                "status": service["status"],
                "region": service["region"],
            }
            for service in self.data["services"]
        ]

    def get_service_health(self, service_name: str) -> dict:
        """Return health details for one service."""

        for service in self.data["services"]:
            if service["service_name"].lower() == service_name.lower():
                return {
                    "found": True,
                    **service,
                }

        return {
            "found": False,
            "message": f"'{service_name}' not found.",
        }

    def get_active_incidents(self, service_name: str | None = None) -> list[dict]:
        """Return active incidents."""

        incidents = self.data["incidents"]

        if service_name:
            incidents = [
                incident
                for incident in incidents
                if incident["service_name"].lower() == service_name.lower()
            ]

        return [
            incident
            for incident in incidents
            if incident["status"] == "ACTIVE"
        ]