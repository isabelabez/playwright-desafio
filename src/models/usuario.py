from dataclasses import dataclass

@dataclass
class UsuarioNovo:
    nome: str
    email: str
    password: str
    administrador: str  # "true" | "false"

@dataclass
class UsuarioAlteracao:
    nome: str
    email: str
    password: str
    administrador: str
