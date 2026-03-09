# src/clients/auth_client.py
from typing import Dict
from playwright.sync_api import APIRequestContext
from src.config import DEFAULT_HEADERS

class AuthClient:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def login(self, email: str, password: str) -> Dict:
        resp = self.request.post(
            "/login",
            data={"email": email, "password": password},
            headers=DEFAULT_HEADERS,
        )
        assert resp.status == 200, f"Login falhou: {resp.status} {resp.text()}"
        return resp.json()  # {"message":"Login realizado com sucesso","authorization":"<token>"}