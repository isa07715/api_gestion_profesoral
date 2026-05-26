"""
estudio_ac_servicio.py - Servicio para la tabla estudio_ac.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.estudio_ac_repositorio import EstudioACRepositorio


class EstudioACServicio:
    """Servicio para operaciones de negocio de estudio_ac."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = EstudioACRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, estudio: int, area_conocimiento: int) -> Optional[dict]:
        """Obtiene un registro por PK compuesta."""
        return await self._repo.obtener_por_id(estudio, area_conocimiento)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo registro."""
        return await self._repo.crear(datos)
    
    async def update(self, estudio: int, area_conocimiento: int, datos: dict) -> bool:
        """Actualiza un registro (no aplica)."""
        return await self._repo.actualizar(estudio, area_conocimiento, datos)
    
    async def delete(self, estudio: int, area_conocimiento: int) -> bool:
        """Elimina un registro."""
        return await self._repo.eliminar(estudio, area_conocimiento)
    
    async def get_by_estudio(self, estudio: int) -> list[dict]:
        """Obtiene todas las areas de conocimiento de un estudio."""
        return await self._repo.obtener_por_estudio(estudio)
    
    async def get_by_area(self, area_conocimiento: int) -> list[dict]:
        """Obtiene todos los estudios de un area de conocimiento."""
        return await self._repo.obtener_por_area(area_conocimiento)