# tests/ui/admin/test_admin_crud_produtos.py
import pytest

@pytest.mark.admin
def test_admin_crud_produto(admin_products_page, produtos_client, produto_payload):
    # Pré-condição opcional via API: nenhum produto com esse nome (só exemplo)
    # Execução via UI
    admin_products_page.open()
    admin_products_page.novo_produto(
        nome=produto_payload["nome"],
        preco=produto_payload["preco"],
        descricao=produto_payload["descricao"],
        quantidade=produto_payload["quantidade"],
    )

    # Editar o primeiro produto na lista
    admin_products_page.editar_produto_primeiro(novo_nome=produto_payload["nome"] + " - EDITADO")

    # Excluir o primeiro produto
    admin_products_page.excluir_produto_primeiro()