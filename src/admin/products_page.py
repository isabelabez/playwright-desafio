from pages.base_page import BasePage
from pages.components.navbar import NavBar
from playwright.async_api import expect

class AdminProductsPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self.nav = NavBar(self._page)

    async def open_list(self):
        await self.nav.open_menu("Listar Produtos")
        await expect(self._page.get_by_role("heading", name="Lista de Produtos")).to_be_visible()

    async def open_create(self):
        await self.nav.open_menu("Cadastrar Produtos")
        await expect(self._page.get_by_role("heading", name="Cadastro de Produto")).to_be_visible()

    async def add

    async def delete(self, product_name: str):
        # exemplo: clicar no botão de deletar do produto específico
        delete_btn = self._page.get_by_role("button", name=f"Deletar {product_name}")
        await expect(delete_btn).to_be_visible()
        await delete_btn.click()
        # confirmar deleção, se necessário
        await expect(self._page.get_by_text(f"{product_name} deletado")).to_be_visible()
