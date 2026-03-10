import pytest
from funktion import accept_cookies, search_product, select_product
from playwright.sync_api import expect

def test_filtrering(page):
    # Gå till startsidan
    page.goto("https://www.inet.se/")

    # Acceptera cookies
    accept_cookies(page)

    # Sök efter en produktkategori
    search_product(page, "Laptops")

    # Välj första produkten i sökresultatet
    select_product(page, "Lenovo IdeaPad 3")

    # Verifiera att produktsidan laddades korrekt
    product_title = page.locator("h1")
    expect(product_title).to_have_text("Lenovo IdeaPad 3")