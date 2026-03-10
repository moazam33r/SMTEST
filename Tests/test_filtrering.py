# tests/test_filtrering.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from funktion import accept_cookies, search_product
from playwright.sync_api import sync_playwright, expect

def test_filterering():
    """Test: Filtrering fungerar på Inet med 'Bärbar dator'"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            # Gå till webbshopen
            page.goto("https://www.inet.se/")
            
            # Acceptera cookies
            accept_cookies(page)
            
            # Sök efter en produktkategori
            search_product(page, "Laptop")
            
            # Klicka på filter "Bärbar dator"
            filter_laptop = page.locator("text=Bärbar dator")
            filter_laptop.scroll_into_view_if_needed()
            filter_laptop.click()
            
            # Verifiera att filtreringen fungerar
            expect(page.locator("h1")).to_contain_text("Bärbar dator", timeout=5000)
            
            print("Filtreringstestet lyckades: 'Bärbar dator' filter tillämpades korrekt")
        finally:
            browser.close()

if __name__ == "__main__":
    test_filterering()