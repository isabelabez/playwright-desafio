# src/pages/base_page.py  (se já existir, garanta utilitários assim)
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def click_by_testid(self, testid: str):
        self.page.get_by_test_id(testid).click()

    def fill_by_label(self, label: str, value: str):
        self.page.get_by_label(label).fill(value)

    def expect_text(self, text: str):
        self.page.get_by_text(text).wait_for()