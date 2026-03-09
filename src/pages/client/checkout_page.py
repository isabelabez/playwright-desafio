from src.pages.base_page import BasePage
from src.config import FRONT_URL

class CheckoutPage(BasePage):
    URL = f"{FRONT_URL}/checkout"

    def open(self):
        self.goto(self.URL)

    def preencher_endereco_e_confirmar(self, cep: str = "01001000"):
        # Ajuste os labels conforme a UI real
        self.fill_by_label("CEP", cep)
        self.page.get_by_role("button", name="Confirmar").click()

    def assert_compra_concluida(self):
        self.expect_text("Compra concluída")