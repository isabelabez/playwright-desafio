from pages.base_page import BasePage
from playwright.async_api import expect

class CartPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)

    async def assert_item_in_cart(self, name: str):
        await expect(self._page.get_by_role("row", name=name)).to_be_visible()

    async def remove_item(self, name: str):
        row = self._page.get_by_role("row", name=name)
        await row.get_by_role("button", name="Remover").click()

    async def complete_checkout(self):
        """Abstração: finaliza a compra em passos internos."""
        await self._btn("Finalizar Compra").click()
        await self.wait_for_loaded()
        await expect(self._page.get_by_text("Compra concluída")).to_be_visible()