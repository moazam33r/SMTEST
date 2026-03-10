# tests/test_negative_search.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from funktion import accept_cookies, search_product
from playwright.sync_api import sync_playwright, expect

def test_negativ_sok():
    """Negativtest: Sök efter en produkt som inte finns"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            # Gå till webbshopen
            page.goto("https://www.inet.se/")
            
            # Acceptera cookies
            accept_cookies(page)
            
            # Sök efter en produkt som inte finns
            search_product(page, "ööää444")
            
            # Kontrollera felmeddelande
            no_result_msg = page.locator("text=Vi hittade inga resultat som matchade din sökning")
            expect(no_result_msg).to_be_visible(timeout=5000)
            
            print("Negativtestet lyckades: korrekt meddelande visades")
        finally:
            browser.close()

if __name__ == "__main__":
    test_negativ_sok()