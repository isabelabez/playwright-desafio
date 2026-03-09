# src/clients/produtos_client.py
from typing import Any, Dict, Tuple, Optional
from playwright.sync_api import APIRequestContext
from .base_client import BaseCrudClient

class ProdutosClient(BaseCrudClient):
    resource_path = "/produtos"

    def __init__(self, request: APIRequestContext, token: Optional[str] = None):
        super().__init__(request)
        self._auth = {"Authorization": token} if token else {}

    def criar_produto(self, payload: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
        resp = self.request.post(self.resource_path, data=payload, headers=self._auth)
        assert resp.status in (201, 400), f"POST /produtos: {resp.status} {resp.text()}"
        body = resp.json()
        # 201 sucesso -> body["_id"]
        # 400 duplicado -> contrato com mensagem
        return body.get("_id", ""), body

    def obter_por_id(self, prod_id: str):
        return self.request.get(f"{self.resource_path}/{prod_id}")

    def editar_produto(self, prod_id: str, payload: Dict[str, Any]):
        return self.request.put(f"{self.resource_path}/{prod_id}", data=payload, headers=self._auth)

    def deletar_produto(self, prod_id: str):
        return self.request.delete(f"{self.resource_path}/{prod_id}", headers=self._auth)