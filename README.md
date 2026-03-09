# Playwright API + Python (ServeRest)

Projeto exemplo de automação **somente de API** usando **Playwright (Python)** e **pytest**,
seguindo padrão **API/Resource Object** (equivalente a Page Object para UI).

## Pré-requisitos
- Python 3.9+
- Pip

## Instalação
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install
```

## Executar
```bash
pytest -q
```

## Estrutura
```
src/
  clients/
    base_client.py
    usuarios_client.py
  models/
    usuario.py
  config.py

tests/
  conftest.py
  test_usuarios_api.py
```
