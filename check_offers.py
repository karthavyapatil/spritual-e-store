from store.models import Collection
from django.utils import timezone
import datetime

now = timezone.now()
print(f"Current UTC Time: {now}")
print(f"Current Local Time (Kolkata): {timezone.localtime(now)}")

for c in Collection.objects.filter(is_active=True):
    print("---")
    print(f"Collection: {c.title}")
    print(f"Discount: {c.discount_percentage}%")
    print(f"Start: {c.offer_start} (Local: {timezone.localtime(c.offer_start) if c.offer_start else 'None'})")
    print(f"End: {c.offer_end} (Local: {timezone.localtime(c.offer_end) if c.offer_end else 'None'})")
    print(f"Is Applied: {c.is_offer_applied}")
    
    if c.offer_start and c.offer_end:
        should_be_active = c.offer_start <= now <= c.offer_end
        print(f"Condition Match: {should_be_active}")
