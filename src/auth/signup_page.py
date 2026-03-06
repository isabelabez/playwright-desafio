from pages.base_page import BasePage(self):
        await self.goto("/login")
        await self._page.get_by_role("link", name="Cadastre-se").click()
        await expect(self._page.get_by_role("heading", name="Cadastro")).to_be_visible()

    async def register_user(self, name: str, email: str, password: str, admin: bool = False):
        await self.open()
        await self._name.fill(name)
        await self._email.fill(email)
        await self._password.fill(password)
        if admin:
            # se existir toggle/checkbox de administrador
            if await self._is_admin.is_visible():
                await self._is_admin.check()
        await self._register_btn.click()
        await self.wait_for_loaded()
        # Sucesso: redireciona/mostra toast
        await expect(self._page.get_by_text("Cadastro realizado")).to_be_visible()
``
from playwright.async_api import expect

class SignupPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self._name = self._page.get_by_placeholder("Nome").or_(self._page.locator("input[name='nome']"))
        self._email = self._page.get_by_placeholder("Email").or_(self._page.locator("input[type='email']"))
        self._password = self._page.get_by_placeholder("Senha").or_(self._page.locator("input[type='password']"))
        self._is_admin = self._page.get_by_label("Administrador").or_(self._page.locator("input[name='administrador']"))
        self._register_btn = self._btn("Cadastrar")

