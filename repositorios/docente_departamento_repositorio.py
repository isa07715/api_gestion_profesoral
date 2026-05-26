"""
docente_departamento_repositorio.py - Repositorio para la tabla docente_departamento.
"""
from typing import Optional
from repositorios.base_repositorio import BaseRepositorioPostgreSQL


class DocenteDepartamentoRepositorio(BaseRepositorioPostgreSQL):
    """Repositorio para operaciones CRUD de docente_departamento."""
    
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._tabla = "docente_departamento"
    
    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        """Obtiene todos los registros de docente_departamento."""
        query = f"SELECT * FROM {esquema}.{self._tabla} ORDER BY docente, departamento ASC LIMIT {limite}"
        return await self._ejecutar_query(query)
    
    async def obtener_por_id(self, docente: int, departamento: int, esquema: str = "public") -> Optional[dict]:
        """Obtiene un registro por PK compuesta (docente, departamento)."""
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE docente = :docente AND departamento = :departamento"
        resultados = await self._ejecutar_query(query, {"docente": docente, "departamento": departamento})
        return resultados[0] if resultados else None
    
    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        """Crea un nuevo registro en docente_departamento."""
        campos = ", ".join(datos.keys())
        valores = ", ".join([f":{k}" for k in datos.keys()])
        query = f"INSERT INTO {esquema}.{self._tabla} ({campos}) VALUES ({valores})"
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def actualizar(self, docente: int, departamento: int, datos: dict, esquema: str = "public") -> bool:
        """Actualiza un registro existente."""
        set_clause = ", ".join([f"{k} = :{k}" for k in datos.keys()])
        query = f"UPDATE {esquema}.{self._tabla} SET {set_clause} WHERE docente = :docente AND departamento = :departamento"
        datos["docente"] = docente
        datos["departamento"] = departamento
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0
    
    async def eliminar(self, docente: int, departamento: int, esquema: str = "public") -> bool:
        """Elimina un registro por PK compuesta."""
        query = f"DELETE FROM {esquema}.{self._tabla} WHERE docente = :docente AND departamento = :departamento"
        filas = await self._ejecutar_comando(query, {"docente": docente, "departamento": departamento})
        return filas > 0