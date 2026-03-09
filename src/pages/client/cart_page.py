from src.pages.base_page import BasePage

class CartPage(BasePage):
    def finalizar_compra(self):
        self.page.get_by_role("button", name="Finalizar compra").click()