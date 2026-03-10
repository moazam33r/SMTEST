import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from funktion import accept_cookies, search_product, select_product, add_to_cart
from playwright.sync_api import sync_playwright

def test_lagg_i_varukorg():
    with sync_playwright() as p:
        # Starta webbläsaren
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Gå till webbshopen
        page.goto("https://www.inet.se/")
        
        # Anropa funktionerna
        accept_cookies(page)
        search_product(page, "Samsung Galaxy S25")
        select_product(page, "Samsung Galaxy S25 Ultra Silicone Case Grå")
        add_to_cart(page)
        
        # Vänta 3 sekunder så du ser resultatet
        page.wait_for_timeout(3000)
        
        # Stäng webbläsaren
        browser.close()

if __name__ == "__main__":
    test_lagg_i_varukorg()