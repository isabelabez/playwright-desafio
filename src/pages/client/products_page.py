from src.pages.base_page import BasePage
from src.config import FRONT_URL

class ProductsPage(BasePage):
    URL = f"{FRONT_URL}/produtos"

    def open(self):
        self.goto(self.URL, wait_state="domcontentloaded")
        self.wait_network_idle()

    def adicionar_primeiro_produto_ao_carrinho(self):
        # Espera renderizar ao menos um card, depois clica no primeiro botão dentro dele.
        cards = self.page.locator(".card")
        cards.first.wait_for(timeout=15_000)
        cards.first.locator("button").first.wait_for(timeout=15_000)
        cards.first.locator("button").first.click()

    def abrir_carrinho(self):
        # Tente primeiro o link "Carrinho"; se a UI mudar, ajuste para o seletor real da navbar.
        self.page.locator('a:has-text("Carrinho")').first.click()