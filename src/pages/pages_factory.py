# src/pages/pages_factory.py

# Base / componentes
from src.pages.base_page import BasePage
from src.pages.components.navbar import Navbar

# Páginas de domínio que existem de fato hoje
from src.admin.products_page import AdminProductsPage
from src.client.products_page import ClientProductsPage
from src.pages.client.cart_page import CartPage
from src.auth.signup_page import SignupPage

class PagesFactory:
    def __init__(self, page):
        self.page = page

    # base / layout
    def base(self) -> BasePage:
        return BasePage(self.page)

    def navbar(self) -> Navbar:
        return Navbar(self.page)

    # domínios
    def admin_products(self) -> AdminProductsPage:
        return AdminProductsPage(self.page)

    def client_products(self) -> ClientProductsPage:
        return ClientProductsPage(self.page)

    def cart(self) -> CartPage:
        return CartPage(self.page)

    def signup(self) -> SignupPage:
        return SignupPage(self.page)