"""
red_docente_repositorio.py - Repositorio para la tabla red_docente.
"""
from typing import Optional
from repositorios.base_repositorio import BaseRepositorioPostgreSQL


class RedDocenteRepositorio(BaseRepositorioPostgreSQL):
    """Repositorio para operaciones CRUD de red_docente."""
    
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._tabla = "red_docente"
    
    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros de red_docente."""
        query = f"SELECT * FROM {esquema}.{self._tabla} ORDER BY red, docente ASC LIMIT {limite}"
        return await self._ejecutar_query(query)
    
    async def obtener_por_id(self, red: int, docente: int, esquema: str = "public") -> Optional[dict]:
        """Obtiene un registro por PK compuesta (red, docente)."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE red = :red AND docente = :docente"
        resultados = await self._ejecutar_query(query, {"red": red, "docente": docente})
        return resultados[0] if resultados else None
    
    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        """Crea un nuevo registro en red_docente."""
        campos = ", ".join(datos.keys())
        valores = ", ".join([f":{k}" for k in datos.keys()])
        query = f"INSERT INTO {esquema}.{self._tabla} ({campos}) VALUES ({valores})"
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def actualizar(self, red: int, docente: int, datos: dict, esquema: str = "public") -> bool:
        """Actualiza un registro existente."""
        set_clause = ", ".join([f"{k} = :{k}" for k in datos.keys()])
        query = f"UPDATE {esquema}.{self._tabla} SET {set_clause} WHERE red = :red AND docente = :docente"
        datos["red"] = red
        datos["docente"] = docente
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def eliminar(self, red: int, docente: int, esquema: str = "public") -> bool:
        """Elimina un registro por PK compuesta."""
        query = f"DELETE FROM {esquema}.{self._tabla} WHERE red = :red AND docente = :docente"
        filas = await self._ejecutar_comando(query, {"red": red, "docente": docente})
        return filas > 0
    
    async def obtener_por_docente(self, docente: int, esquema: str = "public") -> list[dict]:
        """Obtiene todas las redes de un docente."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE docente = :docente ORDER BY fecha_inicio DESC"
        return await self._ejecutar_query(query, {"docente": docente})
    
    async def obtener_por_red(self, red: int, esquema: str = "public") -> list[dict]:
        """Obtiene todos los docentes de una red."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE red = :red ORDER BY fecha_inicio DESC"
        return await self._ejecutar_query(query, {"red": red})