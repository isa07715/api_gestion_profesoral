"""
docente_servicio.py - Servicio para la tabla docente.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.docente_repositorio import DocenteRepositorio


class DocenteServicio:
    """Servicio para operaciones de negocio de docente."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = DocenteRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los docentes."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, cedula: int) -> Optional[dict]:
        """Obtiene un docente por cedula."""
        return await self._repo.obtener_por_id(cedula)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo docente."""
        return await self._repo.crear(datos)
    
    async def update(self, cedula: int, datos: dict) -> bool:
        """Actualiza un docente."""
        return await self._repo.actualizar(cedula, datos)
    
    async def delete(self, cedula: int) -> bool:
        """Elimina un docente."""
        return await self._repo.eliminar(cedula)