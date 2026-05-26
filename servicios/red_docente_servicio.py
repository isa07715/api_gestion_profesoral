"""
red_docente_servicio.py - Servicio para la tabla red_docente.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.red_docente_repositorio import RedDocenteRepositorio


class RedDocenteServicio:
    """Servicio para operaciones de negocio de red_docente."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = RedDocenteRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, red: int, docente: int) -> Optional[dict]:
        """Obtiene un registro por PK compuesta."""
        return await self._repo.obtener_por_id(red, docente)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo registro."""
        return await self._repo.crear(datos)
    
    async def update(self, red: int, docente: int, datos: dict) -> bool:
        """Actualiza un registro."""
        return await self._repo.actualizar(red, docente, datos)
    
    async def delete(self, red: int, docente: int) -> bool:
        """Elimina un registro."""
        return await self._repo.eliminar(red, docente)
    
    async def get_by_docente(self, docente: int) -> list[dict]:
        """Obtiene todas las redes de un docente."""
        return await self._repo.obtener_por_docente(docente)
    
    async def get_by_red(self, red: int) -> list[dict]:
        """Obtiene todos los docentes de una red."""
        return await self._repo.obtener_por_red(red)