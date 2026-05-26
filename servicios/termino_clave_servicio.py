"""
termino_clave_servicio.py — Servicio para término clave.
"""
from typing import Any


class ServicioTerminoClave:
    """Servicio para operaciones de negocio de término clave."""

    def __init__(self, repositorio):
        self._repo = repositorio

    async def listar(self, limite: int = 1000) -> list[dict]:
        return await self._repo.obtener_todos(limite=limite)

    async def obtener(self, id_valor: Any) -> dict | None:
        return await self._repo.obtener_por_id(id_valor)

    async def crear(self, datos: dict) -> dict | None:
        exito = await self._repo.crear(datos)
        if exito:
            return await self.obtener(datos.get('termino'))
        return None

    async def actualizar(self, id_valor: Any, datos: dict) -> dict | None:
        exito = await self._repo.actualizar(id_valor, datos)
        if exito:
            return await self.obtener(id_valor)
        return None

    async def eliminar(self, id_valor: Any) -> bool:
        return await self._repo.eliminar(id_valor)