from src.pages.base_page import BasePage
from src.config import FRONT_URL

class ProductsPage(BasePage):
    URL = f"{FRONT_URL}/produtos"

    def open(self):
        self.goto(self.URL)

    def adicionar_primeiro_produto_ao_carrinho(self):
    self.page.wait_for_load_state("networkidle")

    # espera algum card de produto existir
    self.page.locator(".card").first.wait_for()

    # clica no botão dentro do primeiro card
    self.page.locator(".card button").first.click()

    def abrir_carrinho(self):
        self.page.locator("a").filter(has_text="Carrinho").click()