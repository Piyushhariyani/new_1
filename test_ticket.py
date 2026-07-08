from src.services.ticket_service import TicketService

service = TicketService()

print("=" * 60)
print("Search OPEN Payment API Tickets")
print("=" * 60)

print(
    service.search_tickets(
        service_name="Payment API",
        status="OPEN",
    )
)

print("\n")

print("=" * 60)
print("Ticket Details")
print("=" * 60)

print(service.get_ticket_details("TKT-1001"))

print("\n")

print("=" * 60)
print("High Priority Tickets")
print("=" * 60)

print(service.get_high_priority_tickets())
