# src/admin/products_page.py (exemplo de assinatura dos métodos)
from src.pages.base_page import BasePage
from src.config import FRONT_URL

class AdminProductsPage(BasePage):
    URL = f"{FRONT_URL}/admin/produtos"

    def open(self):
        self.goto(self.URL)

    def novo_produto(self, nome: str, preco: int, descricao: str, quantidade: int):
        self.page.get_by_role("button", name="Novo").click()
        self.fill_by_label("Nome", nome)
        self.fill_by_label("Preço", str(preco))
        self.fill_by_label("Descrição", descricao)
        self.fill_by_label("Quantidade", str(quantidade))
        self.page.get_by_role("button", name="Salvar").click()

    def editar_produto_primeiro(self, novo_nome: str):
        self.page.get_by_role("button", name="Editar").first.click()
        self.fill_by_label