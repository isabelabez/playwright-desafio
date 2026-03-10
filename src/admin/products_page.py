from src.pages.base_page import BasePage
from src.config import FRONT_URL

class AdminProductsPage(BasePage):
    URL = f"{FRONT_URL}/admin/produtos"

    def open(self):
        self.goto(self.URL, wait_state="domcontentloaded")

    def novo_produto(self, nome: str, preco: int, descricao: str, quantidade: int):
        self.page.get_by_role("button", name="Novo").click()
        self.page.locator('input[name="nome"]').fill(nome)
        self.page.locator('input[name="preco"]').fill(str(preco))
        self.page.locator('textarea[name="descricao"], input[name="descricao"]').fill(descricao)
        self.page.locator('input[name="quantidade"]').fill(str(quantidade))
        self.page.get_by_role("button", name="Salvar").click()

    def editar_produto_primeiro(self, novo_nome: str):
        # Edita o primeiro registro da lista
        self.page.get_by_role("button", name="Editar").first.click()
        self.page.locator('input[name="nome"]').fill(novo_nome)
        self.page.get_by_role("button", name="Salvar").click()

    def excluir_produto_primeiro(self):
        self.page.get_by_role("button", name="Excluir").first.click()
        self.page.get_by_role("button", name="Confirmar").click()