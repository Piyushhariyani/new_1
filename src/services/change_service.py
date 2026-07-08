from __future__ import annotations

from src.config import CHANGE_FILE
from src.utils.json_loader import load_json


class ChangeService:
    """
    Business logic for Change Management operations.
    """

    def __init__(self) -> None:
        self.data = load_json(CHANGE_FILE)

    def list_recent_changes(self) -> list[dict]:
        """
        Return all recent changes.
        """
        return self.data["changes"]

    def get_change_details(self, change_id: str) -> dict:
        """
        Return details of a specific change.
        """

        for change in self.data["changes"]:
            if change["change_id"] == change_id:
                return {
                    "found": True,
                    **change,
                }

        return {
            "found": False,
            "message": f"{change_id} not found."
        }

    def get_changes_for_service(self, service_name: str) -> list[dict]:
        """
        Return all changes for a service.
        """

        return [
            change
            for change in self.data["changes"]
            if change["service_name"].lower() == service_name.lower()
        ]