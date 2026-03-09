# src/config.py
import os

BASE_URL = os.getenv("SERVEREST_BASE_URL", "https://serverest.dev")
DEFAULT_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}