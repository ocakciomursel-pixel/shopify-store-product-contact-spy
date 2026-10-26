"""
Shopify Store Product, Pricing, Stock & Merchant Contact Spy — LangChain, CrewAI & OpenAI Assistants Tool
Official Apify Actor: https://apify.com/lucacelli/shopify-store-product-contact-spy ($0.50 / 1,000 products)
"""
import os
import requests
from typing import Dict, Any, List

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~shopify-store-product-contact-spy/run-sync-get-dataset-items"

def run_shopify_store_product_contact_spy(custom_input: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Executes Shopify Store Product, Pricing, Stock & Merchant Contact Spy on Apify Cloud ($0.50/1k products).
    Scrape complete Shopify product catalogs, variants, SKUs, sale discounts, live stock availability, installed Shopify apps/pixels, and merchant emails & social links without expensive headless browsers.
    """
    default_payload = {
    "storeUrls": [
        "https://gymshark.com",
        "https://allbirds.com"
    ],
    "maxProductsPerStore": 100
}
    payload = custom_input if custom_input else default_payload
    res = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    res.raise_for_status()
    return res.json()
