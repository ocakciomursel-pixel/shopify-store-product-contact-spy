"""
Shopify Store Product, Pricing, Stock & Merchant Contact Spy — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/shopify-store-product-contact-spy ($0.50 / 1,000 products)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~shopify-store-product-contact-spy/run-sync-get-dataset-items"

payload = {
    "storeUrls": [
        "https://gymshark.com",
        "https://allbirds.com"
    ],
    "maxProductsPerStore": 100
}

if __name__ == "__main__":
    print(f"Running Shopify Store Product, Pricing, Stock & Merchant Contact Spy on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])
