from src.pages.base_page import BasePage
from src.config import FRONT_URL

class CheckoutPage(BasePage):
    URL = f"{FRONT_URL}/checkout"

    def open(self):
        self.goto(self.URL, wait_state="domcontentloaded")

    def preencher_endereco_e_confirmar(self, cep: str = "01001000"):
        # Ajuste seletores conforme o formulário real
        # Ex.: name="cep" / placeholder="CEP"
        self.page.locator('input[name="cep"], input[placeholder*="CEP"]').first.fill(cep)
        self.page.get_by_role("button", name="Confirmar").click()

    def assert_compra_concluida(self):
        # Mensagem final
        self.expect_text("Compra concluída")