from src.clients.usuarios_client import UsuariosClient


def test_post_criar_usuario(
    usuarios_client: UsuariosClient,
    payload_usuario_unico
):
    user_id, body = usuarios_client.criar_usuario(payload_usuario_unico)
    assert user_id


def test_get_listar_usuario(
    usuarios_client: UsuariosClient,
    usuario_criado_id
):
    resp = usuarios_client.listar_por_id(usuario_criado_id)
    assert resp.ok
    data = resp.json()
    assert "usuarios" in data


def test_put_editar_usuario(
    usuarios_client: UsuariosClient,
    usuario_criado_id,
    payload_usuario_unico
):
    novo_payload = {
        **payload_usuario_unico,
        "nome": payload_usuario_unico["nome"] + " - EDITADO"
    }
    body = usuarios_client.editar_usuario(usuario_criado_id, novo_payload)
    assert "message" in body