from playwright.sync_api import Page, expect
import re

def accept_cookies(page: Page):
    """Acceptera cookies"""
    try:
        page.locator("[data-test-id='cookie_accept']").click()
        print("Cookies accepterade")
    except:
        print("Ingen cookie-popup hittades")

def search_product(page: Page, search_term: str):
    """Sök efter en produkt"""
    page.locator("[data-test-id='search_input']").fill(search_term)
    page.locator("[data-test-id='search_input']").press("Enter")
    print(f"Sökte efter: {search_term}")

def select_product(page: Page, product_name: str):
    """Välj en specifik produkt från sökresultatet"""
    page.get_by_role("heading", name=product_name).click()
    print(f"Valde produkt: {product_name}")

def add_to_cart(page: Page):
    """Lägg till produkt i varukorgen"""
    page.locator("div.b1ejavog:has-text('Lägg i kundvagn')").click()
    print("Produkt tillagd i varukorgen")

def go_to_checkout(page: Page):
    """Gå vidare till kassan"""
    page.locator("[data-test-id='to_checkout_button']").click()
    print("Gick vidare till kassan")

def complete_checkout_flow(page: Page, search_term: str, product_name: str):
    """Komplett flöde: acceptera cookies -> sök -> välj produkt -> lägg i kundvagn -> gå till kassan"""
    
    accept_cookies(page)
    search_product(page, search_term)
    select_product(page, product_name)
    add_to_cart(page)
    go_to_checkout(page)
    
    # Verifiera att vi är på kassasidan
    expect(page).to_have_url(re.compile(r".*kassa.*"))
    print("Är nu på kassasidan med kunduppgifter")