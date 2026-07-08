from fastmcp import FastMCP

from src.services.ticket_service import TicketService

mcp = FastMCP("support-ticket")

service = TicketService()


@mcp.tool
def search_tickets(
    service_name: str | None = None,
    status: str | None = None,
) -> list[dict]:
    """
    Search support tickets.
    """
    return service.search_tickets(
        service_name=service_name,
        status=status,
    )


@mcp.tool
def get_ticket_details(ticket_id: str) -> dict:
    """
    Get ticket details.
    """
    return service.get_ticket_details(ticket_id)


@mcp.tool
def get_high_priority_tickets() -> list[dict]:
    """
    Return OPEN P1/P2 tickets.
    """
    return service.get_high_priority_tickets()


if __name__ == "__main__":
    mcp.run()