import re
from src.pages.base_page import BasePage
from src.config import FRONT_URL

class LoginPage(BasePage):
    URL = f"{FRONT_URL}/login"

    def open(self):
        self.goto(self.URL, wait_state="domcontentloaded")

    def login(self, email: str, password: str):
        self.page.locator('input[name="email"]').fill(email)
        self.page.locator('input[name="password"]').fill(password)
        self.page.get_by_role("button", name="Entrar").click()

    def assert_logado(self):
        # Estratégias:
        # 1) se a UI tiver o botão/link "Sair"
        try:
            self.page.get_by_text("Sair", exact=False).wait_for(timeout=8_000)
            return
        except Exception:
            pass

        # 2) ou verificar redirecionamento (ajuste o padrão conforme sua navegação real):
        self.page.wait_for_url(re.compile(r".*/(produtos|home|)"), timeout=10_000)