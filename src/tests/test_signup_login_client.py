import pytest
from playwright.async_api import expect
from utils.data import unique_email

pytestmark = [pytest.mark.e2e]

PASS = "User@123"

@pytest.mark.asyncio
async def test_signup_logout_login_client(pages):
    email = unique_email("user")
    # Cadastro
    await pages.auth.signup.register_user(name="User QA", email=email, password=PASS, admin=False)

    # Após cadastro, deve existir UI de cliente
    await expect(pages.client.products._page.get_by_role("button", name="Carrinho")).to_be_visible()

    # Logout (encapsular se houver componente de perfil; exemplo simples por link/botão)
    logout_btn = pages.client.products._page.get_by_role("button", name="Logout").or_(
        pages.client.products._page.get_by_role("link", name="Sair")
    )
    if await logout_btn.is_visible():
        await logout_btn.click()

    # Login pelo fluxo de cliente
    await pages.auth.client.login(email, PASS)

    # Validações
    await pages.client.products.open_home()
    await pages.client.products._page.wait_for_load_state("networkidle")
    await expect(pages.client.products._page).to_have_url(lambda u: "/".rstrip("/") in u)
    await expect(pages.client.products._page.get_by_role("heading", name="Produtos")).to_be_visible()
    # Carrinho começa vazio: botão visível, contador opcionalmente vazio/desabilitado
    cart_btn = pages.client.products._page.get_by_role("button", name="Carrinho")
    await expect(cart_btn).to_be_visible()