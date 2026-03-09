# tests/ui/cadastro/test_signup_login_logout.py
import pytest

@pytest.mark.cadastro
def test_signup_login_logout(signup_page, login_page, usuario_payload):
    # Cadastro via UI
    signup_page.open()
    signup_page.cadastrar(
        nome=usuario_payload["nome"],
        email=usuario_payload["email"],
        password=usuario_payload["password"],
        admin=False,
    )

    # Login via UI
    login_page.open()
    login_page.login(usuario_payload["email"], usuario_payload["password"])

    # Alguma asserção de que logou (ex.: saudação ou menu do usuário)
    login_page.page.get_by_text(usuario_payload["nome"]).wait_for(timeout=5000)

    # Logout via UI
    login_page.logout()