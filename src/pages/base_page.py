from playwright.async_api import Page, expect

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self._page = page          # Encapsulamento: não exponha o page
        self._base_url = base_url

    async def goto(self, path: str = "/"):
        await self._page.goto(f"{self._base_url}{path}")

    async def wait_for_loaded(self):
        # Abstração: espera genérica de carregamento
        await self._page.wait_for_load_state("networkidle")

    async def assert_url_contains(self, fragment: str):
        await expect(self._page).to_have_url(lambda url: fragment in url)  # to_have_url condicional

    # Utilidades de seleção “limpas”
    def _btn(self, name: str):
        return self._page.get_by_role("button", name=name)

    def _link(self, name: str):
        return self._page.get_by_role("link", name=name)