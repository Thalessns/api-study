"""Modulo principal do projeto."""

from fastapi import FastAPI, status

from src.usuarios.router import usuarios_router

api = FastAPI(
    title="Study API",
    description="API de estudos",
    version="0.0.1",
    prefix="/api"
)


@api.get("/", status_code=status.HTTP_200_OK)
async def root() -> dict[str, str]:
    """Endpoint raiz da API.
    
    Returns:
        dict[str, str]: Mensagem de sucesso.
    """
    return {"message": "Welcome to the Study API"}


api.include_router(usuarios_router)
