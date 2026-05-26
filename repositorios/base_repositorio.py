"""
base_repositorio.py - Clase base para repositorios PostgreSQL.
Proporciona métodos genéricos para operaciones CRUD.
"""
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncConnection
from sqlalchemy import text
from typing import Any


class BaseRepositorioPostgreSQL:
    """Clase base para todos los repositorios PostgreSQL."""

    def __init__(self, cadena_conexion: str):
        """Inicializa el motor de base de datos."""
        self._cadena_conexion = cadena_conexion
        self._engine: AsyncEngine | None = None

    async def _obtener_engine(self) -> AsyncEngine:
        """Obtiene o crea el motor de base de datos (singleton por instancia)."""
        if self._engine is None:
            self._engine = create_async_engine(
                self._cadena_conexion,
                echo=False,
                pool_pre_ping=True,
                pool_size=5,
                max_overflow=10
            )
        return self._engine

    async def _ejecutar_query(self, query: str, params: dict[str, Any] | None = None) -> list[dict]:
        """Ejecuta una query SELECT y retorna los resultados como lista de diccionarios."""        
        engine = await self._obtener_engine()
        async with engine.connect() as conn:
            result = await conn.execute(text(query), params or {})
            await conn.commit()
            filas = result.fetchall()
            return [dict(fila._mapping) for fila in filas]

    async def _ejecutar_comando(self, query: str, params: dict[str, Any] | None = None) -> int:    
        """Ejecuta un comando (INSERT, UPDATE, DELETE) y retorna filas afectadas."""
        engine = await self._obtener_engine()
        async with engine.connect() as conn:
            result = await conn.execute(text(query), params or {})
            await conn.commit()
            return result.rowcount or 0

    async def cerrar(self):
        """Cierra el motor de base de datos."""
        if self._engine:
            await self._engine.dispose()
            self._engine = None