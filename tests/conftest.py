import pytest
import time
import random
from playwright.sync_api import Page, APIRequestContext

from src.clients.auth_client import AuthClient
from src.clients.produtos_client import ProdutosClient
from src.config import API_URL, DEFAULT_HEADERS

# ---------------- API ----------------

@pytest.fixture(scope="session")
def api_request_context(playwright) -> APIRequestContext:
    request = playwright.request.new_context(
        base_url=API_URL,
        extra_http_headers=DEFAULT_HEADERS
    )
    yield request
    request.dispose()

@pytest.fixture(scope="session")
def admin_token(api_request_context):
    auth = AuthClient(api_request_context)
    # ⚠️ ajuste para um admin válido do serverest.dev
    response = auth.login("admin@admin.com", "admin123")
    return response["authorization"]

@pytest.fixture
def produtos_client(api_request_context, admin_token):
    return ProdutosClient(api_request_context, token=admin_token)

# ---------------- DATA ----------------

@pytest.fixture
def usuario_payload():
    sufixo = f"{int(time.time())}{random.randint(100,999)}"
    return {
        "nome": f"Usuario {sufixo}",
        "email": f"usuario{sufixo}@qa.com.br",
        "password": "teste123",
        "administrador": "false"
    }

# ---------------- UI PAGES ----------------

from src.pages.auth.login_page import LoginPage
from src.pages.auth.signup_page import SignupPage
from src.pages.client.products_page import ProductsPage
from src.pages.client.cart_page import CartPage
from src.pages.client.checkout_page import CheckoutPage
from src.admin.products_page import AdminProductsPage

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def signup_page(page: Page):
    return SignupPage(page)

@pytest.fixture
def products_page(page: Page):
    return ProductsPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page: Page):
    return CheckoutPage(page)

@pytest.fixture
def admin_products_page(page: Page):
    return AdminProductsPage(page)