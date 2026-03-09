# src/config.py
import os

# UI (front público do ServeRest)
FRONT_URL = os.getenv("FRONT_URL", "https://front.serverest.dev")

# API (ambiente online do ServeRest - rotas públicas)
API_URL = os.getenv("SERVEREST_BASE_URL", "https://serverest.dev")

DEFAULT_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}