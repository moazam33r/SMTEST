from playwright.sync_api import sync_playwright, Page

def launch_browser():
    """Startar Playwright och öppnar en ny sida."""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)  # headless=True för tyst körning
    page = browser.new_page()
    return playwright, browser, page

def accept_cookies(page: Page):
    """Acceptera cookies om popupen visas."""
    cookie_button = page.locator('button[data-test-id="cookie_accept"]')
    if cookie_button.is_visible():
        cookie_button.click()
        page.wait_for_load_state("networkidle")

def open_inet_homepage(page: Page):
    """Navigera till startsidan och acceptera cookies."""
    page.goto("https://www.inet.se/")
    page.wait_for_load_state("networkidle")
    accept_cookies(page)
    return page.title()

def apply_filter(page: Page, filter_name: str):
    """Klicka på ett filter på produktsidan."""
    filter_selector = f"text={filter_name}"
    page.locator(filter_selector).click()
    page.wait_for_load_state("networkidle")

def search_product(page: Page, search_text: str):
    """Skriver in söktext i sökrutan och trycker Enter."""
    search_box = page.locator('input[data-test-id="search-input"]')
    search_box.fill(search_text)
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")