# src/clients/base_client.py
from abc import ABC
from playwright.sync_api import APIRequestContext
from typing import Any, Dict, Optional, Callable
import time

class BaseCrudClient(ABC):
    resource_path: str

    def __init__(self, request: APIRequestContext):
        self.request = request

    # --- util de retry para 5xx ---
    def _with_retry(self, fn: Callable, url: str, **kwargs):
        last = None
        for attempt in range(1, 4):  # 3 tentativas
            resp = fn(url, **kwargs)
            last = resp
            if resp.status < 500:    # 2xx/4xx: não é erro de infra
                return resp
            time.sleep(0.5 * attempt)  # backoff simples: 0.5s, 1s
        return last

    def create(self, payload: Dict[str, Any]):
        return self._with_retry(self.request.post, self.resource_path, data=payload)

    def list(self, params: Optional[Dict[str, Any]] = None):
        return self._with_retry(self.request.get, self.resource_path, params=params or {})

    def retrieve(self, _id: str):
        return self._with_retry(self.request.get, f"{self.resource_path}/{_id}")

    def update(self, _id: str, payload: Dict[str, Any]):
        return self._with_retry(self.request.put, f"{self.resource_path}/{_id}", data=payload)

    def delete(self, _id: str):
        return self._with_retry(self.request.delete, f"{self.resource_path}/{_id}")