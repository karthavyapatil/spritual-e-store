import os
import django
import sys

# Setup Django environment
sys.path.append('e:\\Sharp\\New-Yuganter-Store')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yugantar_Store.settings')
django.setup()

from store.models import Product, ProductVariation

def check_variations():
    print("Checking latest products and their variations...")
    # Get the last 5 products updated
    products = Product.objects.all().order_by('-updated_at')[:5]
    
    if not products.exists():
        print("No products found.")
        return

    for p in products:
        print(f"\nProduct: {p.title} (ID: {p.id})")
        variations = p.product_variations.all()
        print(f"Variation Count: {variations.count()}")
        if variations.exists():
            for v in variations:
                print(f" - Variation ID: {v.id}, Value: {v.variation_option.value}, Price: {v.price}, Stock: {v.variation_stock}")
        else:
            print(" - No variations found.")

if __name__ == "__main__":
    check_variations()
