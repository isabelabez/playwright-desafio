import pytest
from utils.data import unique_email

pytestmark = [pytest.mark.e2e]

CLIENT_PASS = "Client@123"

@pytest.mark.asyncio
async def test_client_add_items_and_complete_checkout(pages):
    # Arrange: cadastrar cliente e logar (polimorfismo: ClientLoginPage.login)
    client_email = unique_email("client")
    await pages.auth.signup.register_user(
        name="Cliente QA", email=client_email, password=CLIENT_PASS, admin=False
    )
    await pages.auth.client.login(client_email, CLIENT_PASS)

    # Act: abrir home e adicionar 2 itens
    await pages.client.products.open_home()
    # Em catálogos dinâmicos, escolha por nome conhecido ou primeiro card visível
    # Aqui, exemplificando por nome; adapte ao catálogo atual:
    await pages.client.products.add_to_cart_by_card_name("Mouse")     # toContainText
    await pages.client.products.add_to_cart_by_card_name("Teclado")

    await pages.client.products.go_to_cart()
    await pages.client.cart.assert_item_in_cart("Mouse")
    await pages.client.cart.assert_item_in_cart("Teclado")

    # Abstração principal
    await pages.client.cart.complete_checkout()