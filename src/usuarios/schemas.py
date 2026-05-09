""""Schemas para usuarios."""

from pydantic import BaseModel, field_validator


class Usuario(BaseModel):

    nome: str 
    email: str
    senha: str | int

    @field_validator("senha", mode="before")
    def validar_senha(value: str | int) -> str | int:
        if isinstance(value, bool):
            raise ValueError("A senha não pode ser um valor booleano.")
        return value
