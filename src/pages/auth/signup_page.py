from src.pages.base_page import BasePage
from src.config import FRONT_URL

class SignupPage(BasePage):
    URL = f"{FRONT_URL}/cadastrarusuarios"

    def open(self):
        self.goto(self.URL)

    def cadastrar(self, nome: str, email: str, password: str, admin: bool = False):
    self.page.wait_for_load_state("domcontentloaded")

    self.page.locator('input[name="nome"]').fill(nome)
    self.page.locator('input[name="email"]').fill(email)
    self.page.locator('input[name="password"]').fill(password)

    if admin:
        self.page.locator('input[type="checkbox"]').check()

    self.page.get_by_role("button", name="Cadastrar").click()