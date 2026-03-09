# tests/ui/checkout/test_checkout_cliente.py
import pytest

@pytest.mark.checkout
def test_checkout_cliente(products_page, cart_page, checkout_page):
    # Listagem de produtos
    products_page.open()
    products_page.adicionar_primeiro_produto_ao_carrinho()
    products_page.abrir_carrinho()

    # Carrinho → Checkout
    cart_page.finalizar_compra()
    # (caso a UI leve direto para checkout)
    # checkout_page.open()  # use se houver rota direta

    # Preencher e confirmar
    checkout_page.preencher_endereco_e_confirmar(cep="01001000")
    checkout_page.assert_compra_concluida()