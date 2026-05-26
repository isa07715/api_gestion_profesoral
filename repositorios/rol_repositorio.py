from repositorios.base_repositorio import BaseRepositorioPostgreSQL

class RepositorioRolPostgreSQL(BaseRepositorioPostgreSQL):
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._esquema = "public"
        self._tabla = "rol"

    async def obtener_todos(self, limite: int = 1000) -> list[dict]:
        # ✅ Incluye fecha_creacion en el SELECT
        query = f"""
            SELECT id, nombre, descripcion, activo, fecha_creacion 
            FROM {self._esquema}.{self._tabla} 
            ORDER BY id 
            LIMIT :limite
        """
        return await self._ejecutar_query(query, {"limite": limite})

    async def obtener_por_id(self, id: int) -> dict | None:
        # ✅ Incluye fecha_creacion en el SELECT
        query = f"""
            SELECT id, nombre, descripcion, activo, fecha_creacion 
            FROM {self._esquema}.{self._tabla} 
            WHERE id = :id
        """
        res = await self._ejecutar_query(query, {"id": id})
        return res[0] if res else None

    async def crear(self, datos: dict) -> dict | None:
        # ✅ RETORNA id Y fecha_creacion para que FastAPI no falle
        query = f"""
            INSERT INTO {self._esquema}.{self._tabla} (nombre, descripcion, activo)
            VALUES (:nombre, :descripcion, :activo)
            RETURNING id, fecha_creacion
        """
        try:
            res = await self._ejecutar_query(query, datos)
            return res[0] if res else None  # Retorna el diccionario completo
        except Exception as e:
            print(f"❌ Error al crear rol: {e}")
            return None

    async def actualizar(self, id: int, datos: dict) -> bool:
        datos["id"] = id
        query = f"""
            UPDATE {self._esquema}.{self._tabla}
            SET nombre = :nombre, descripcion = :descripcion, activo = :activo
            WHERE id = :id
        """
        return (await self._ejecutar_comando(query, datos)) > 0

    async def eliminar(self, id: int) -> bool:
        query = f"DELETE FROM {self._esquema}.{self._tabla} WHERE id = :id"
        try:
            return (await self._ejecutar_comando(query, {"id": id})) > 0
        except Exception:
            return False