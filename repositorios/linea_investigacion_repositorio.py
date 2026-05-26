from repositorios.base_repositorio import BaseRepositorioPostgreSQL

class RepositorioLineaInvestigacionPostgreSQL(BaseRepositorioPostgreSQL):
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._esquema = "public"
        self._tabla = "linea_investigacion"

    async def obtener_todos(self, limite: int = 1000) -> list[dict]:
        query = f"""
            SELECT id, nombre, descripcion 
            FROM {self._esquema}.{self._tabla} 
            ORDER BY id 
            LIMIT :limite
        """
        return await self._ejecutar_query(query, {"limite": limite})

    async def obtener_por_id(self, id: int) -> dict | None:
        query = f"""
            SELECT id, nombre, descripcion 
            FROM {self._esquema}.{self._tabla} 
            WHERE id = :id
        """
        res = await self._ejecutar_query(query, {"id": id})
        return res[0] if res else None

    async def crear(self, datos: dict) -> int | None:
        query = f"""
            INSERT INTO {self._esquema}.{self._tabla} (nombre, descripcion)
            VALUES (:nombre, :descripcion)
            RETURNING id
        """
        try:
            res = await self._ejecutar_query(query, datos)
            return res[0]['id'] if res else None
        except Exception as e:
            print(f"❌ Error al crear línea: {e}")
            return None

    async def actualizar(self, id: int, datos: dict) -> bool:
        datos["id"] = id
        query = f"""
            UPDATE {self._esquema}.{self._tabla}
            SET nombre = :nombre, descripcion = :descripcion
            WHERE id = :id
        """
        return (await self._ejecutar_comando(query, datos)) > 0

    async def eliminar(self, id: int) -> bool:
        query = f"DELETE FROM {self._esquema}.{self._tabla} WHERE id = :id"
        try:
            return (await self._ejecutar_comando(query, {"id": id})) > 0
        except Exception:
            return False