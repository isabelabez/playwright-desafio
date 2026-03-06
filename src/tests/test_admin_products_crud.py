import pytest
from playwright.async_api import expect
from utils.data import unique_email, unique_name

pytestmark = [pytest.mark.e2e]

ADMIN_PASS = "Admin@123"

@pytest.mark.asyncio
async def test_admin_products_crud(pages):
    # Arrange: criar um admin novo via cadastro UI
    admin_email = unique_email("admin")
    await pages.auth.signup.register_user(
        name="Admin QA", email=admin_email, password=ADMIN_PASS, admin=True
    )
    # Polimorfismo: ambos têm login(), mas AdminLoginPage valida menus administrativos
    await pages.auth.admin.login(admin_email, ADMIN_PASS)

    # Act: Cadastrar produto
    product_name = unique_name("Produto QA")
    await pages.admin.products.add(
        name=product_name, price=199, description="Produto de teste", quantity=10
    )

    # Assert: está na lista
    await pages.admin.products.assert_in_list(product_name)

    # Editar
    new_name = product_name + "-EDIT"
    await pages.admin.products.edit_by_name(product_name, new_name)
    await pages.admin.products.assert_in_list(new_name)

    # Excluir
    await pages.admin.products.remove_by_name(new_name)

    # Validação negativa: linha não deve existir (simplificada)
    await pages.admin.products.open_list()
    await expect(pages.admin.products._page.get_by_role("row", name=new_name)).not_to_be_visible()
    