from repositorios.beca_repositorio import RepositorioBecaPostgreSQL
from servicios.conexion.proveedor_conexion import get_proveedor_conexion

class BecaServicio:
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = RepositorioBecaPostgreSQL(proveedor.obtener_cadena_conexion())

    async def get_all(self, limite: int = 1000) -> list[dict]:
        return await self._repo.obtener_todos(limite=limite)

    async def create(self, datos: dict) -> bool:
        return await self._repo.crear(datos)

    async def update(self, estudios_id: int, datos: dict) -> bool:
        return await self._repo.actualizar(estudios_id, datos)

    async def delete(self, estudios_id: int) -> bool:
        return await self._repo.eliminar(estudios_id)