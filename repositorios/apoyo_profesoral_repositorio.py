from repositorios.base_repositorio import BaseRepositorioPostgreSQL

class ApoyoProfesoralRepositorio(BaseRepositorioPostgreSQL):
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._esquema = "public"
        self._tabla = "apoyo_profesoral"

    async def obtener_todos(self, limite: int = 1000) -> list[dict]:
        # Unimos con estudios_realizados para mostrar el título del estudio en la lista
        query = f"""
            SELECT ap.estudios, ap.con_apoyo, ap.institucion, ap.tipo, 
                   er.titulo as nombre_estudio
            FROM {self._esquema}.{self._tabla} ap
            LEFT JOIN public.estudios_realizados er ON ap.estudios = er.id
            ORDER BY ap.estudios
            LIMIT :limite
        """
        return await self._ejecutar_query(query, {"limite": limite})

    async def obtener_por_estudio(self, estudios_id: int) -> dict | None:
        query = f"""
            SELECT estudios, con_apoyo, institucion, tipo
            FROM {self._esquema}.{self._tabla}
            WHERE estudios = :estudios_id
        """
        res = await self._ejecutar_query(query, {"estudios_id": estudios_id})
        return res[0] if res else None

    async def crear(self, datos: dict) -> bool:
        query = f"""
            INSERT INTO {self._esquema}.{self._tabla} 
            (estudios, con_apoyo, institucion, tipo)
            VALUES (:estudios, :con_apoyo, :institucion, :tipo)
            ON CONFLICT (estudios) DO UPDATE 
            SET con_apoyo = EXCLUDED.con_apoyo, 
                institucion = EXCLUDED.institucion, 
                tipo = EXCLUDED.tipo
        """
        try:
            # Usamos comando porque no retornamos ID
            filas = await self._ejecutar_comando(query, datos)
            return filas > 0
        except Exception as e:
            print(f"❌ Error al crear apoyo: {e}")
            return False

    async def actualizar(self, estudios_id: int, datos: dict) -> bool:
        datos["estudios"] = estudios_id
        query = f"""
            UPDATE {self._esquema}.{self._tabla}
            SET con_apoyo = :con_apoyo, institucion = :institucion, tipo = :tipo
            WHERE estudios = :estudios
        """
        return (await self._ejecutar_comando(query, datos)) > 0

    async def eliminar(self, estudios_id: int) -> bool:
        query = f"DELETE FROM {self._esquema}.{self._tabla} WHERE estudios = :estudios_id"
        try:
            return (await self._ejecutar_comando(query, {"estudios_id": estudios_id})) > 0
        except Exception:
            return False