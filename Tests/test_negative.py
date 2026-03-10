# tests/test_negative.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from funktion import accept_cookies, search_product
from playwright.sync_api import sync_playwright, expect

def test_negativ_sok():
    """Negativtest: Sök efter en sträng som inte finns och verifiera felmeddelande"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False så man ser webbläsaren
        page = browser.new_page()
        
        # Gå till Inet
        page.goto("https://www.inet.se/")
        
        # Acceptera cookies
        accept_cookies(page)
        
        # Använd search_product för negativt test
        search_product(page, "ääöö3423")
        
        # Kontrollera att meddelande om inga resultat visas
        no_result_msg = page.locator("text=Vi hittade inga resultat som matchade din sökning")
        expect(no_result_msg).to_be_visible()
        
        print("Negativtestet lyckades: korrekt meddelande visades för ogiltig sökning")
        
        browser.close()