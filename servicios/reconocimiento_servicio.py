"""
reconocimiento_servicio.py - Servicio para la tabla reconocimiento.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.reconocimiento_repositorio import ReconocimientoRepositorio


class ReconocimientoServicio:
    """Servicio para operaciones de negocio de reconocimiento."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = ReconocimientoRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los reconocimientos."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, id: int) -> Optional[dict]:
        """Obtiene un reconocimiento por id."""
        return await self._repo.obtener_por_id(id)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo reconocimiento."""
        return await self._repo.crear(datos)
    
    async def update(self, id: int, datos: dict) -> bool:
        """Actualiza un reconocimiento."""
        return await self._repo.actualizar(id, datos)
    
    async def delete(self, id: int) -> bool:
        """Elimina un reconocimiento."""
        return await self._repo.eliminar(id)
    
    async def get_by_docente(self, docente: int) -> list[dict]:
        """Obtiene todos los reconocimientos de un docente."""
        return await self._repo.obtener_por_docente(docente)