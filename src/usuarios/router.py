"""Rotas de usuários."""

from fastapi import APIRouter, status

from src.usuarios.schemas import Usuario

usuarios_router = APIRouter(prefix="/usuarios")


@usuarios_router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_usuario(dados: Usuario) -> Usuario:
    """Cria um novo usuário.

    Returns:
        dict: Mensagem de sucesso.
    """
    return dados
