"""
estudio_ac_repositorio.py - Repositorio para la tabla estudio_ac.
"""
from typing import Optional
from repositorios.base_repositorio import BaseRepositorioPostgreSQL


class EstudioACRepositorio(BaseRepositorioPostgreSQL):
    """Repositorio para operaciones CRUD de estudio_ac."""
    
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._tabla = "estudio_ac"
    
    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros de estudio_ac."""
        query = f"SELECT * FROM {esquema}.{self._tabla} ORDER BY estudio, area_conocimiento ASC LIMIT {limite}"
        return await self._ejecutar_query(query)
    
    async def obtener_por_id(self, estudio: int, area_conocimiento: int, esquema: str = "public") -> Optional[dict]:
        """Obtiene un registro por PK compuesta (estudio, area_conocimiento)."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE estudio = :estudio AND area_conocimiento = :area_conocimiento"
        resultados = await self._ejecutar_query(query, {"estudio": estudio, "area_conocimiento": area_conocimiento})
        return resultados[0] if resultados else None
    
    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        """Crea un nuevo registro en estudio_ac."""
        campos = ", ".join(datos.keys())
        valores = ", ".join([f":{k}" for k in datos.keys()])
        query = f"INSERT INTO {esquema}.{self._tabla} ({campos}) VALUES ({valores})"
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def actualizar(self, estudio: int, area_conocimiento: int, datos: dict, esquema: str = "public") -> bool:
        """Actualiza un registro existente (no aplica para esta tabla)."""
        return False
    
    async def eliminar(self, estudio: int, area_conocimiento: int, esquema: str = "public") -> bool:
        """Elimina un registro por PK compuesta."""
        query = f"DELETE FROM {esquema}.{self._tabla} WHERE estudio = :estudio AND area_conocimiento = :area_conocimiento"
        filas = await self._ejecutar_comando(query, {"estudio": estudio, "area_conocimiento": area_conocimiento})
        return filas > 0
    
    async def obtener_por_estudio(self, estudio: int, esquema: str = "public") -> list[dict]:
        """Obtiene todas las areas de conocimiento de un estudio."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE estudio = :estudio ORDER BY area_conocimiento ASC"
        return await self._ejecutar_query(query, {"estudio": estudio})
    
    async def obtener_por_area(self, area_conocimiento: int, esquema: str = "public") -> list[dict]:
        """Obtiene todos los estudios de un area de conocimiento."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE area_conocimiento = :area_conocimiento ORDER BY estudio ASC"
        return await self._ejecutar_query(query, {"area_conocimiento": area_conocimiento})