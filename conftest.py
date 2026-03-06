import pytest
import pytest_asyncio
from types import SimpleNamespace
from playwright.async_api import async_playwright

# Se você TINHA uma fixture event_loop customizada, remova-a por ora.
# O pytest-asyncio em modo STRICT já gerencia o event loop.

# ---- Playwright: browser/context/page (async) ----
@pytest_asyncio.fixture(scope="session")
async def browser():
    async with async_playwright() as p:
        # Ajuste headless conforme sua necessidade:
        browser = await p.chromium.launch(headless=True)
        yield browser
        await browser.close()

@pytest_asyncio.fixture
async def context(browser):
    ctx = await browser.new_context()
    yield ctx
    await ctx.close()

@pytest_asyncio.fixture
async def page(context):
    pg = await context.new_page()
    # Se tiver uma URL base, pode navegar aqui:
    # await pg.goto("http://localhost:3000/")
    yield pg
    await pg.close()

# ---- Fixture 'pages' esperada pelos testes ----
@pytest_asyncio.fixture
async def pages(page):
    """
    Devolve um namespace com a estrutura usada nos testes:
      pages.auth.signup, pages.auth.client, pages.auth.admin,
      pages.client.products, pages.client.cart,
      pages.admin.products
    """
    # Importa POs que EXISTEM hoje na sua árvore:
    from src.auth.signup_page import SignupPage
    from src.client.products_page import ClientProductsPage
    from src.pages.client.cart_page import CartPage
    from src.admin.products_page import AdminProductsPage

    # Stubs mínimos de Login (pois estes arquivos ainda não existem na árvore):
    class ClientLoginPage:
        def __init__(self, pg):
            self._page = pg

        async def login(self, email: str, password: str):
            # TODO: ajuste URL e seletores aos reais da sua app
            await self._page.goto("http://localhost:3000/login")
            await self._page.get_by_label("Email").fill(email)
            await self._page.get_by_label("Senha").fill(password)
            await self._page.get_by_role("button", name="Entrar").click()

    class AdminLoginPage(ClientLoginPage):
        async def login(self, email: str, password: str):
            await super().login(email, password)
            # Aqui você pode validar elementos específicos do menu/admin se quiser

    return SimpleNamespace(
        auth=SimpleNamespace(
            signup=SignupPage(page),
            client=ClientLoginPage(page),
            admin=AdminLoginPage(page),
        ),
        client=SimpleNamespace(
            products=ClientProductsPage(page),
            cart=CartPage(page),
        ),
        admin=SimpleNamespace(
            products=AdminProductsPage(page),
        ),
    )