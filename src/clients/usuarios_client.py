from typing import Dict, Any
from .base_client import BaseCrudClient

class UsuariosClient(BaseCrudClient):
    resource_path = "/usuarios"

    def criar_usuario(self, payload: Dict[str, Any]):
        resp = self.create(payload)
        assert resp.status == 201, f"Esperado 201 ao cadastrar, veio {resp.status}"
        body = resp.json()
        assert "_id" in body, "Resposta de cadastro não possui _id"
        return body["_id"], body

    def listar_por_id(self, _id: str):
        return self.list(params={"_id": _id})

    def editar_usuario(self, _id: str, payload: Dict[str, Any]):
        resp = self.update(_id, payload)
        assert resp.status in (200, 201), f"PUT deve retornar 200/201, veio {resp.status}"
        return resp.json()
