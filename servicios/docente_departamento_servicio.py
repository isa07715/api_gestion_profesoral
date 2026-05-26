"""
docente_departamento_servicio.py - Servicio para la tabla docente_departamento.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.docente_departamento_repositorio import DocenteDepartamentoRepositorio


class DocenteDepartamentoServicio:
    """Servicio para operaciones de negocio de docente_departamento."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = DocenteDepartamentoRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, docente: int, departamento: int) -> Optional[dict]:
        """Obtiene un registro por PK compuesta."""
        return await self._repo.obtener_por_id(docente, departamento)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo registro."""
        return await self._repo.crear(datos)
    
    async def update(self, docente: int, departamento: int, datos: dict) -> bool:
        """Actualiza un registro."""
        return await self._repo.actualizar(docente, departamento, datos)
    
    async def delete(self, docente: int, departamento: int) -> bool:
        """Elimina un registro."""
        return await self._repo.eliminar(docente, departamento)