from fastmcp import FastMCP

from src.services.change_service import ChangeService

mcp = FastMCP("change-management")

service = ChangeService()


@mcp.tool
def list_recent_changes() -> list[dict]:
    """
    List recent changes.
    """
    return service.list_recent_changes()


@mcp.tool
def get_change_details(change_id: str) -> dict:
    """
    Get change details.
    """
    return service.get_change_details(change_id)


@mcp.tool
def get_changes_for_service(service_name: str) -> list[dict]:
    """
    Return all changes for a service.
    """
    return service.get_changes_for_service(service_name)


if __name__ == "__main__":
    mcp.run()