import pytest
import time
import random
from playwright.sync_api import Playwright, APIRequestContext

from src.config import BASE_URL, DEFAULT_HEADERS
from src.clients.usuarios_client import UsuariosClient


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> APIRequestContext:
    """
    Contexto de requisições HTTP do Playwright (APIRequestContext).
    """
    request = playwright.request.new_context(
        base_url=BASE_URL,
        extra_http_headers=DEFAULT_HEADERS,
    )
    yield request
    request.dispose()


@pytest.fixture
def usuarios_client(api_request_context: APIRequestContext) -> UsuariosClient:
    """
    Client de alto nível para a API de Usuários.
    """
    return UsuariosClient(api_request_context)


@pytest.fixture
def payload_usuario_unico():
    """
    Payload válido e único para criação de usuário.
    """
    sufixo = f"{int(time.time())}{random.randint(1000,9999)}"
    return {
        "nome": f"QA Playwright {sufixo}",
        "email": f"qa.playwright.{sufixo}@qa.com.br",
        "password": "senha123",
        "administrador": "false",
    }


@pytest.fixture
def usuario_criado_id(
    usuarios_client: UsuariosClient,
    payload_usuario_unico
):
    """
    Cria um usuário antes do teste e devolve apenas o ID.
    """
    user_id, _ = usuarios_client.criar_usuario(payload_usuario_unico)
    return user_id