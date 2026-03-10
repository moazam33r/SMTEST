# tests/test_filtrering.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from funktion import accept_cookies, search_product
from playwright.sync_api import sync_playwright, expect

def test_filterering():
    """Test att filtrering fungerar på Inet"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.inet.se/")

        # Acceptera cookies
        accept_cookies(page)

        # Sök efter exempelprodukt
        search_product(page, "Laptop")

        # Klicka på filter "Gaming" (exempel på filter)
        filter_gaming = page.locator("text=Gaming")
        filter_gaming.scroll_into_view_if_needed()
        filter_gaming.click()

        # Verifiera att filtreringen fungerar
        expect(page.locator("h1")).to_contain_text("Gaming")

        browser.close()