from repositorios.apoyo_profesoral_repositorio import ApoyoProfesoralRepositorio
from servicios.conexion.proveedor_conexion import get_proveedor_conexion

class ApoyoProfesoralServicio:
    def __init__(self):
        proveedor = get_proveedor_conexion()
        self._repo = ApoyoProfesoralRepositorio(proveedor.obtener_cadena_conexion())

    async def get_all(self, limite: int = 1000) -> list[dict]:
        return await self._repo.obtener_todos(limite=limite)

    async def get_by_estudio(self, estudios_id: int) -> dict | None:
        return await self._repo.obtener_por_estudio(estudios_id)

    async def create(self, datos: dict) -> bool:
        return await self._repo.crear(datos)

    async def update(self, estudios_id: int, datos: dict) -> bool:
        return await self._repo.actualizar(estudios_id, datos)

    async def delete(self, estudios_id: int) -> bool:
        return await self._repo.eliminar(estudios_id)