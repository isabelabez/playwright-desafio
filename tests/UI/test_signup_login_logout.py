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

    
# Asserção robusta de login concluído:
login_page.assert_logado()


# Logout via UI
login_page.logout()