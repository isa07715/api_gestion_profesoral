"""
docente_repositorio.py - Repositorio para la tabla docente.
"""
from typing import Optional
from repositorios.base_repositorio import BaseRepositorioPostgreSQL


class DocenteRepositorio(BaseRepositorioPostgreSQL):
    """Repositorio para operaciones CRUD de docente."""
    
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._tabla = "docente"
        self._pk = "cedula"
    
    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        """Obtiene todos los docentes."""
        query = f"SELECT * FROM {esquema}.{self._tabla} ORDER BY {self._pk} ASC LIMIT {limite}"
        return await self._ejecutar_query(query)
    
    async def obtener_por_id(self, cedula: int, esquema: str = "public") -> Optional[dict]:
        """Obtiene un docente por cedula."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE {self._pk} = :cedula"
        resultados = await self._ejecutar_query(query, {"cedula": cedula})
        return resultados[0] if resultados else None
    
    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        """Crea un nuevo docente."""
        campos = ", ".join(datos.keys())
        valores = ", ".join([f":{k}" for k in datos.keys()])
        query = f"INSERT INTO {esquema}.{self._tabla} ({campos}) VALUES ({valores})"
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def actualizar(self, cedula: int, datos: dict, esquema: str = "public") -> bool:
        """Actualiza un docente existente."""
        set_clause = ", ".join([f"{k} = :{k}" for k in datos.keys()])
        query = f"UPDATE {esquema}.{self._tabla} SET {set_clause} WHERE {self._pk} = :cedula"
        datos["cedula"] = cedula
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def eliminar(self, cedula: int, esquema: str = "public") -> bool:
        """Elimina un docente por cedula."""
        query = f"DELETE FROM {esquema}.{self._tabla} WHERE {self._pk} = :cedula"
        filas = await self._ejecutar_comando(query, {"cedula": cedula})
        return filas > 0