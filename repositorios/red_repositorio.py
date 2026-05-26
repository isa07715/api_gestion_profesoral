"""
red_repositorio.py — Repositorio para red.
PK es 'idr'.
"""
from repositorios.base_repositorio import BaseRepositorioPostgreSQL
from typing import Any


class RepositorioRedPostgreSQL(BaseRepositorioPostgreSQL):
    """Repositorio concreto para red académica en PostgreSQL."""

    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._tabla = "red"
        self._pk = "idr"

    async def obtener_todos(self, esquema: str = "public", limite: int = 1000) -> list[dict]:
        query = f"SELECT * FROM {esquema}.{self._tabla} LIMIT :limite"
        return await self._ejecutar_query(query, {"limite": limite})

    async def obtener_por_id(self, id_valor: Any, esquema: str = "public") -> dict | None:
        query = f"SELECT * FROM {esquema}.{self._tabla} WHERE {self._pk} = :id"
        resultados = await self._ejecutar_query(query, {"id": id_valor})
        return resultados[0] if resultados else None

    async def crear(self, datos: dict, esquema: str = "public") -> bool:
        query = f"""
            INSERT INTO {esquema}.{self._tabla} (idr, nombre, url, pais)
            VALUES (:idr, :nombre, :url, :pais)
        """
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0

    async def actualizar(self, id_valor: Any, datos: dict, esquema: str = "public") -> bool:
        campos = ", ".join([f"{k} = :{k}" for k in datos.keys()])
        query = f"UPDATE {esquema}.{self._tabla} SET {campos} WHERE {self._pk} = :id"
        datos["id"] = id_valor
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0

    async def eliminar(self, id_valor: Any, esquema: str = "public") -> bool:
        query = f"DELETE FROM {esquema}.{self._tabla} WHERE {self._pk} = :id"
        filas = await self._ejecutar_comando(query, {"id": id_valor})
        return filas > 0