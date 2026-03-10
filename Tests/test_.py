from SMTEST.funktion import launch_browser, open_inet_homepage, apply_filter, search_product

# 1️⃣ Positivt test – filtrering
def test_filter_functionality():
    playwright, browser, page = launch_browser()
    open_inet_homepage(page)

    # Filtrera på exempel: "Stationära datorer"
    apply_filter(page, "Stationära datorer")

    # Kontrollera att URL eller sidtitel innehåller filtreringen
    assert "stationära" in page.url.lower(), "Filtreringen fungerar inte korrekt"

    browser.close()
    playwright.stop()

# 2️⃣ Negativt test – ogiltig sökning
def test_negative_search():
    playwright, browser, page = launch_browser()
    open_inet_homepage(page)

    # Sök på ogiltig text
    search_product(page, "ääöö3423")

    # Verifiera att meddelande om inga resultat visas
    no_results = page.locator('text=Vi hittade inga resultat som matchade din sökning')
    assert no_results.is_visible(), "Negativt test misslyckades: meddelande om inga resultat visas inte"

    browser.close()
    playwright.stop()