"""
i_repositorio.py — Interfaz genérica para repositorios (Protocol).
Define el contrato que deben cumplir todos los repositorios.
"""
from typing import Protocol, Any


class IRepositorio(Protocol):
    """Interfaz genérica para repositorios."""

    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros de la tabla."""
        ...

    async def obtener_por_id(self, id_valor: Any, esquema: str = "public") -> dict | None:
        """Obtiene un registro por su ID."""
        ...

    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        """Crea un nuevo registro."""
        ...

    async def actualizar(self, id_valor: Any, datos: dict, esquema: str = "public") -> bool:
        """Actualiza un registro existente."""
        ...

    async def eliminar(self, id_valor: Any, esquema: str = "public") -> bool:
        """Elimina un registro (borrado lógico)."""
        ...