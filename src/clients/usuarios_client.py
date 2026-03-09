from typing import Any, Dict, Tuple
from playwright.sync_api import APIRequestContext
from .base_client import BaseCrudClient

class UsuariosClient(BaseCrudClient):
    resource_path = "/usuarios"

    def __init__(self, request: APIRequestContext):
        super().__init__(request)

    def criar_usuario(self, payload: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
        resp = self.create(payload)
        assert resp.status == 201, f"Esperado 201, veio {resp.status}. Body: {resp.text()}"
        body = resp.json()
        return body.get("_id"), body

    def listar_por_id(self, user_id: str):
        resp = self.retrieve(user_id)
        return resp

    def editar_usuario(self, user_id: str, payload: Dict[str, Any]):
        resp = self.update(user_id, payload)
        assert resp.status in (200, 204), f"PUT esperado 200/204, veio {resp.status}. Body: {resp.text()}"
        try:
            return resp.json()
        except Exception:
            return {}
