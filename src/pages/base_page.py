from typing import Optional
from playwright.sync_api import Page, Locator

DEFAULT_TIMEOUT = 10_000  # 10s

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(DEFAULT_TIMEOUT)

    def goto(self, url: str, wait_state: str = "domcontentloaded"):
        self.page.goto(url)
        self.page.wait_for_load_state(wait_state)

    def wait_network_idle(self):
        # usado por páginas de lista/católogos onde há várias chamadas XHR/Fetch
        self.page.wait_for_load_state("networkidle")

    def expect_text(self, text: str, timeout: Optional[int] = None):
        self.page.get_by_text(text, exact=False).wait_for(timeout=timeout)

    def fill_by_label(self, label: str, value: str):
        self.page.get_by_label(label, exact=False).fill(value)

    def click_by_text(self, text: str):
        self.page.get_by_text(text, exact=False).click()

    def click_has_text(self, selector: str, text: str):
        self.page.locator(selector).filter(has_text=text).first.click()

    def within(self, container_selector: str) -> Locator:
        return self.page.locator(container_selector)