"""
i_servicio.py — Interfaz genérica para servicios (Protocol).
Define el contrato que deben cumplir todos los servicios.
"""
from typing import Protocol, Any


class IServicio(Protocol):
    """Interfaz genérica para servicios."""

    async def listar(self, limite: int = 1000) -> list[dict]:
        """Lista todos los registros."""
        ...

    async def obtener(self, id_valor: Any) -> dict | None:
        """Obtiene un registro por ID."""
        ...

    async def crear(self, datos: dict) -> dict | None:
        """Crea un nuevo registro."""
        ...

    async def actualizar(self, id_valor: Any, datos: dict) -> dict | None:
        """Actualiza un registro existente."""
        ...

    async def eliminar(self, id_valor: Any) -> bool:
        """Elimina un registro."""
        ...