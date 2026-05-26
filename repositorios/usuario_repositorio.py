from repositorios.base_repositorio import BaseRepositorioPostgreSQL

class UsuarioRepositorio(BaseRepositorioPostgreSQL):
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._esquema = "public"
        self._tabla = "usuario"

    async def obtener_todos(self, limite: int = 1000) -> list[dict]:
        query = f"""
            SELECT id, username, password, email, nombre_completo, activo, 
                   fecha_creacion, fecha_actualizacion 
            FROM {self._esquema}.{self._tabla} 
            ORDER BY id 
            LIMIT :limite
        """
        return await self._ejecutar_query(query, {"limite": limite})

    async def obtener_por_id(self, id: int) -> dict | None:
        query = f"""
            SELECT id, username, password, email, nombre_completo, activo, 
                   fecha_creacion, fecha_actualizacion 
            FROM {self._esquema}.{self._tabla} 
            WHERE id = :id
        """
        res = await self._ejecutar_query(query, {"id": id})
        return res[0] if res else None

    async def crear(self, datos: dict) -> dict | None:
        # ✅ IMPORTANTE: La variable 'datos' se pasa al query
        query = f"""
            INSERT INTO {self._esquema}.{self._tabla} 
            (username, password, email, nombre_completo, activo, fecha_actualizacion)
            VALUES (:username, :password, :email, :nombre_completo, :activo, NOW())
            RETURNING id, fecha_creacion, fecha_actualizacion
        """
        try:
            # ✅ AQUÍ ESTABA EL ERROR: Usamos 'datos', NO 'data'
            res = await self._ejecutar_query(query, datos)
            return res[0] if res else None
        except Exception as e:
            print(f"❌ Error Repo Usuario: {e}")
            return None

    async def actualizar(self, id: int, datos: dict) -> bool:
        datos["id"] = id
        query = f"""
            UPDATE {self._esquema}.{self._tabla}
            SET username = :username, password = :password, email = :email, 
                nombre_completo = :nombre_completo, activo = :activo,
                fecha_actualizacion = NOW()
            WHERE id = :id
        """
        # ✅ AQUÍ TAMBIÉN: Usamos 'datos'
        return (await self._ejecutar_comando(query, datos)) > 0

    async def eliminar(self, id: int) -> bool:
        query = f"DELETE FROM {self._esquema}.{self._tabla} WHERE id = :id"
        try:
            return (await self._ejecutar_comando(query, {"id": id})) > 0
        except Exception:
            return False