from repositorios.experiencia_repositorio import ExperienciaRepositorio
from servicios.conexion.proveedor_conexion import get_proveedor_conexion

class ExperienciaServicio:
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = ExperienciaRepositorio(proveedor.obtener_cadena_conexion())

    async def get_all(self, limite: int = 1000) -> list[dict]:
        return await self._repo.obtener_todos(limite=limite)

    async def get_by_id(self, id: int) -> dict | None:
        return await self._repo.obtener_por_id(id)

    async def create(self, datos: dict) -> int | None:
        return await self._repo.crear(datos)

    async def update(self, id: int, datos: dict) -> bool:
        return await self._repo.actualizar(id, datos)

    async def delete(self, id: int) -> bool:
        return await self._repo.eliminar(id)