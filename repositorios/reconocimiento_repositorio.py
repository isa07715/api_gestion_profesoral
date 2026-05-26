"""
reconocimiento_repositorio.py - Repositorio para la tabla reconocimiento.
"""
from typing import Optional
from repositorios.base_repositorio import BaseRepositorioPostgreSQL


class ReconocimientoRepositorio(BaseRepositorioPostgreSQL):
    """Repositorio para operaciones CRUD de reconocimiento."""
    
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._tabla = "reconocimiento"
        self._pk = "id"
    
    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        """Obtiene todos los reconocimientos."""
        query = f"SELECT * FROM {esquema}.{self._tabla} ORDER BY {self._pk} ASC LIMIT {limite}"
        return await self._ejecutar_query(query)
    
    async def obtener_por_id(self, id: int, esquema: str = "public") -> Optional[dict]:
        """Obtiene un reconocimiento por id."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE {self._pk} = :id"
        resultados = await self._ejecutar_query(query, {"id": id})
        return resultados[0] if resultados else None
    
    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        """Crea un nuevo reconocimiento."""
        campos = ", ".join(datos.keys())
        valores = ", ".join([f":{k}" for k in datos.keys()])
        query = f"INSERT INTO {esquema}.{self._tabla} ({campos}) VALUES ({valores})"
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def actualizar(self, id: int, datos: dict, esquema: str = "public") -> bool:
        """Actualiza un reconocimiento existente."""
        set_clause = ", ".join([f"{k} = :{k}" for k in datos.keys()])
        query = f"UPDATE {esquema}.{self._tabla} SET {set_clause} WHERE {self._pk} = :id"
        datos["id"] = id
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def eliminar(self, id: int, esquema: str = "public") -> bool:
        """Elimina un reconocimiento por id."""
        query = f"DELETE FROM {esquema}.{self._tabla} WHERE {self._pk} = :id"
        filas = await self._ejecutar_comando(query, {"id": id})
        return filas > 0
    
    async def obtener_por_docente(self, docente: int, esquema: str = "public") -> list[dict]:
        """Obtiene todos los reconocimientos de un docente."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE docente = :docente ORDER BY fecha DESC"
        return await self._ejecutar_query(query, {"docente": docente})