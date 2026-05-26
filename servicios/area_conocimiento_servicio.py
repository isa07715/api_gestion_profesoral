"""
area_conocimiento_servicio.py — Servicio para área de conocimiento.
Capa de negocio: valida reglas y delega al repositorio.
"""
from typing import Any


class ServicioAreaConocimiento:
    """Servicio para operaciones de negocio de área de conocimiento."""

    def __init__(self, repositorio):
        """Inyección de dependencia del repositorio."""
        self._repo = repositorio

    async def listar(self, limite: int = 1000) -> list[dict]:
        """Lista todas las áreas de conocimiento."""
        return await self._repo.obtener_todos(limite=limite)

    async def obtener(self, id_valor: Any) -> dict | None:
        """Obtiene un área de conocimiento por ID."""
        return await self._repo.obtener_por_id(id_valor)

    async def crear(self, datos: dict) -> dict | None:
        """Crea un nuevo área de conocimiento."""
        # Validaciones de negocio aquí
        exito = await self._repo.crear(datos)
        if exito:
            return await self.obtener(datos.get('id'))
        return None

    async def actualizar(self, id_valor: Any, datos: dict) -> dict | None:
        """Actualiza un área de conocimiento."""
        # Validaciones de negocio aquí
        exito = await self._repo.actualizar(id_valor, datos)
        if exito:
            return await self.obtener(id_valor)
        return None

    async def eliminar(self, id_valor: Any) -> bool:
        """Elimina un área de conocimiento."""
        return await self._repo.eliminar(id_valor)