import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from funktion import accept_cookies, search_product, select_product, add_to_cart, go_to_checkout
from playwright.sync_api import sync_playwright
from fixtures import fake_customer

def test_kassa():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.inet.se/")
        
        accept_cookies(page)
        search_product(page, "Samsung Galaxy S25")
        select_product(page, "Samsung Galaxy S25 Ultra Silicone Case Grå")
        add_to_cart(page)
        go_to_checkout(page)
        
        # Vänta att sidan laddas
        page.wait_for_timeout(2000)
        
        # Hämta falsk kunddata
        kund = fake_customer()
        
        # Bocka i checkbox för "inget telefonnummer"
        page.get_by_role("checkbox", name="Inget telefonnummer").check()
        
        # Fyll i övriga kunduppgifter
        page.locator("#organizationNo").fill(kund["personnummer"])
        page.locator("#firstName").fill(kund["first_name"])
        page.locator("#lastName").fill(kund["last_name"])
        page.locator("#streetAddress").fill(kund["street"])
        page.locator("#zipCode").fill(kund["postcode"])
        
        # Vänta så du ser resultatet
        page.wait_for_timeout(5000)
        browser.close()
        
        print("Test klart")

if __name__ == "__main__":
    test_kassa()