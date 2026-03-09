from src.pages.base_page import BasePage
from src.config import FRONT_URL

class LoginPage(BasePage):
    URL = f"{FRONT_URL}/login"

    def open(self):
        self.goto(self.URL)

    def login(self, email: str, password: str):
        # Ajuste os labels/roles conforme a UI real do front.serverest.dev
        self.fill_by_label("Email", email)
        self.fill_by_label("Senha", password)
        self.page.get_by_role("button", name="Entrar").click()

    def logout(self):
        # Exemplo: ajuste conforme a UI
        self.page.get_by_role("button", name="Sair").click()