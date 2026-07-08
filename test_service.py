from src.services.service_health_service import ServiceHealthService

service = ServiceHealthService()

print("=" * 50)
print("All Services")
print("=" * 50)
print(service.list_services())

print("\n" + "=" * 50)
print("Payment API Health")
print("=" * 50)
print(service.get_service_health("Payment API"))

print("\n" + "=" * 50)
print("Payment API Active Incidents")
print("=" * 50)
print(service.get_active_incidents("Payment API"))
