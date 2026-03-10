import pytest
from funktion import accept_cookies, search_product
from playwright.sync_api import expect

def test_negativ_sok(page):
    # Gå till startsidan
    page.goto("https://www.inet.se/")

    # Acceptera cookies
    accept_cookies(page)

    # Sök efter en ogiltig produkt
    search_product(page, "ääöö3423")

    # Verifiera att meddelande om inga resultat visas
    result_text = page.locator("text=Vi hittade inga resultat som matchade din sökning")
    expect(result_text).to_be_visible()