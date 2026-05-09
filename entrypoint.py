"""Módulo de inicialização do projeto."""

import uvicorn

uvicorn.run(
    "src.app:api",
    host="0.0.0.0",
    port=8001,
    reload=False
)
