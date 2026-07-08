from fastmcp import FastMCP

from src.services.service_health_service import ServiceHealthService

mcp = FastMCP("service-health")

service = ServiceHealthService()


@mcp.tool
def list_services() -> list[dict]:
    """
    List all enterprise services.
    """
    return service.list_services()


@mcp.tool
def get_service_health(service_name: str) -> dict:
    """
    Get detailed health of a service.
    """
    return service.get_service_health(service_name)


@mcp.tool
def get_active_incidents(service_name: str | None = None) -> list[dict]:
    """
    Return active incidents.
    """
    return service.get_active_incidents(service_name)


if __name__ == "__main__":
    mcp.run()