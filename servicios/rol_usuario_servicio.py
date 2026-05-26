"""
rol_usuario_servicio.py - Servicio para la tabla rol_usuario.
"""
from typing import Optional
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from repositorios.rol_usuario_repositorio import RolUsuarioRepositorio


class RolUsuarioServicio:
    """Servicio para operaciones de negocio de rol_usuario."""
    
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = RolUsuarioRepositorio(proveedor.obtener_cadena_conexion())
    
    async def get_all(self, limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros."""
        return await self._repo.obtener_todos(limite=limite)
    
    async def get_by_id(self, usuario_id: int, rol_id: int) -> Optional[dict]:
        """Obtiene un registro por PK compuesta."""
        return await self._repo.obtener_por_id(usuario_id, rol_id)
    
    async def create(self, datos: dict) -> bool:
        """Crea un nuevo registro."""
        return await self._repo.crear(datos)
    
    async def update(self, usuario_id: int, rol_id: int, datos: dict) -> bool:
        """Actualiza un registro (no aplica)."""
        return await self._repo.actualizar(usuario_id, rol_id, datos)
    
    async def delete(self, usuario_id: int, rol_id: int) -> bool:
        """Elimina un registro."""
        return await self._repo.eliminar(usuario_id, rol_id)
    
    async def get_by_usuario(self, usuario_id: int) -> list[dict]:
        """Obtiene todos los roles de un usuario."""
        return await self._repo.obtener_por_usuario(usuario_id)
    
    async def get_by_rol(self, rol_id: int) -> list[dict]:
        """Obtiene todos los usuarios de un rol."""
        return await self._repo.obtener_por_rol(rol_id)