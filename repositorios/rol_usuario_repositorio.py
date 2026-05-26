"""
rol_usuario_repositorio.py - Repositorio para la tabla rol_usuario.
"""
from typing import Optional
from repositorios.base_repositorio import BaseRepositorioPostgreSQL


class RolUsuarioRepositorio(BaseRepositorioPostgreSQL):
    """Repositorio para operaciones CRUD de rol_usuario."""
    
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._tabla = "rol_usuario"
    
    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros de rol_usuario."""
        query = f"SELECT * FROM {esquema}.{self._tabla} ORDER BY usuario_id, rol_id ASC LIMIT {limite}"
        return await self._ejecutar_query(query)
    
    async def obtener_por_id(self, usuario_id: int, rol_id: int, esquema: str = "public") -> Optional[dict]:
        """Obtiene un registro por PK compuesta."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE usuario_id = :usuario_id AND rol_id = :rol_id"
        resultados = await self._ejecutar_query(query, {"usuario_id": usuario_id, "rol_id": rol_id})
        return resultados[0] if resultados else None
    
    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        """Crea un nuevo registro en rol_usuario."""
        campos = ", ".join(datos.keys())
        valores = ", ".join([f":{k}" for k in datos.keys()])
        query = f"INSERT INTO {esquema}.{self._tabla} ({campos}) VALUES ({valores})"
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def actualizar(self, usuario_id: int, rol_id: int, datos: dict, esquema: str = "public") -> bool:
        """Actualiza un registro existente (no aplica)."""
        return False
    
    async def eliminar(self, usuario_id: int, rol_id: int, esquema: str = "public") -> bool:
        """Elimina un registro por PK compuesta."""
        query = f"DELETE FROM {esquema}.{self._tabla} WHERE usuario_id = :usuario_id AND rol_id = :rol_id"
        filas = await self._ejecutar_comando(query, {"usuario_id": usuario_id, "rol_id": rol_id})
        return filas > 0
    
    async def obtener_por_usuario(self, usuario_id: int, esquema: str = "public") -> list[dict]:
        """Obtiene todos los roles de un usuario."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE usuario_id = :usuario_id ORDER BY rol_id ASC"
        return await self._ejecutar_query(query, {"usuario_id": usuario_id})
    
    async def obtener_por_rol(self, rol_id: int, esquema: str = "public") -> list[dict]:
        """Obtiene todos los usuarios de un rol."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE rol_id = :rol_id ORDER BY usuario_id ASC"
        return await self._ejecutar_query(query, {"rol_id": rol_id})