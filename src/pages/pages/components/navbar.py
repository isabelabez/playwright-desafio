from playwright.async_api import Page, expect

class NavBar:
    def __init__(self, page: Page):
        self._page = page
        # os seletores ficam escondidos aqui
        self._menu_button = lambda name: self._page.get_by_role("link", name=name)

    async def open_menu(self, name: str):
        await expect(self._menu_button(name)).to_be_visible()
        await self._menu_button(name).click()

    async def assert_logged_in_as_admin(self):
        # itens típicos do admin, segundo o README do front (Usuários/Produtos/Relatórios)
        await expect(self._menu_button("Listar Produtos")).to_be_visible()
        await expect(self._menu_button("Listar Usuários")).to_be_visible()