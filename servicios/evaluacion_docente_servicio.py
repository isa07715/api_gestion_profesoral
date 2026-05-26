"""
evaluacion_docente_servicio.py - Servicio para la tabla evaluacion_docente.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.evaluacion_docente_repositorio import EvaluacionDocenteRepositorio


class EvaluacionDocenteServicio:
    """Servicio para operaciones de negocio de evaluacion_docente."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = EvaluacionDocenteRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todas las evaluaciones."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, id: int) -> Optional[dict]:
        """Obtiene una evaluacion por id."""
        return await self._repo.obtener_por_id(id)
    
    async def create(self, datos: dict) -> bool:
        """Crea una nueva evaluacion."""
        return await self._repo.crear(datos)
    
    async def update(self, id: int, datos: dict) -> bool:
        """Actualiza una evaluacion."""
        return await self._repo.actualizar(id, datos)
    
    async def delete(self, id: int) -> bool:
        """Elimina una evaluacion."""
        return await self._repo.eliminar(id)
    
    async def get_by_docente(self, docente: int) -> list[dict]:
        """Obtiene todas las evaluaciones de un docente."""
        return await self._repo.obtener_por_docente(docente)