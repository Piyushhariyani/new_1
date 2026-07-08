from src.services.change_service import ChangeService

service = ChangeService()

print("=" * 60)
print("Recent Changes")
print("=" * 60)

print(service.list_recent_changes())

print("\n")

print("=" * 60)
print("Change Details")
print("=" * 60)

print(service.get_change_details("CHG-2001"))

print("\n")

print("=" * 60)
print("Payment API Changes")
print("=" * 60)

print(service.get_changes_for_service("Payment API"))