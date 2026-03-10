from src.pages.base_page import BasePage

class CartPage(BasePage):
    def finalizar_compra(self):
        # Se for modal/página dedicada de carrinho, espere elementos chave antes
        self.page.get_by_role("button", name="Finalizar compra").click()