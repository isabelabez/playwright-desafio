from pages.base_page import BasePage
from pages.components.navbar import NavBar
from playwright.async_api import expect

class ClientProductsPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self.nav = NavBar(self._page)

    async def open_home(self):
        await self.goto("/")  # home lista produtos
        await self.wait_for_loaded()
        await expect(self._page.get_by_role("heading", name="Produtos")).to_be_visible()

    async def add_to_cart_by_card_name(self, name: str):
        card = self._page.get_by_role("article", name=name).or_(self._page.get_by_text(name).locator(".."))
        await expect(card).to_be_visible()
        await card.get_by_role("button", name="Adicionar").click()

    async def go_to_cart(self):
        await self._page.get_by_role("button", name="Carrinho").click()
        await expect(self._page.get_by_role("heading", name="Seu Carrinho")).to_be_visible()