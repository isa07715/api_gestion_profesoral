from repositorios.base_repositorio import BaseRepositorioPostgreSQL

class RepositorioBecaPostgreSQL(BaseRepositorioPostgreSQL):
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._esquema = "public"
        self._tabla = "beca"

    async def obtener_todos(self, limite: int = 1000) -> list[dict]:
        query = f"""
            SELECT b.estudios, b.tipo, b.institucion, b.fecha_inicio, b.fecha_fin,
                   er.titulo as nombre_estudio
            FROM {self._esquema}.{self._tabla} b
            LEFT JOIN public.estudios_realizados er ON b.estudios = er.id
            ORDER BY b.estudios
            LIMIT :limite
        """
        return await self._ejecutar_query(query, {"limite": limite})

    async def crear(self, datos: dict) -> bool:
        # Si ya existe una beca para ese estudio, la actualiza (Upsert)
        query = f"""
            INSERT INTO {self._esquema}.{self._tabla} 
            (estudios, tipo, institucion, fecha_inicio, fecha_fin)
            VALUES (:estudios, :tipo, :institucion, :fecha_inicio, :fecha_fin)
            ON CONFLICT (estudios) DO UPDATE 
            SET tipo = EXCLUDED.tipo, 
                institucion = EXCLUDED.institucion,
                fecha_inicio = EXCLUDED.fecha_inicio,
                fecha_fin = EXCLUDED.fecha_fin
        """
        try:
            filas = await self._ejecutar_comando(query, datos)
            return filas > 0
        except Exception as e:
            print(f"❌ Error Repo Beca: {e}")
            return False

    async def actualizar(self, estudios_id: int, datos: dict) -> bool:
        datos["estudios"] = estudios_id
        query = f"""
            UPDATE {self._esquema}.{self._tabla}
            SET tipo = :tipo, institucion = :institucion, 
                fecha_inicio = :fecha_inicio, fecha_fin = :fecha_fin
            WHERE estudios = :estudios
        """
        return (await self._ejecutar_comando(query, datos)) > 0

    async def eliminar(self, estudios_id: int) -> bool:
        query = f"DELETE FROM {self._esquema}.{self._tabla} WHERE estudios = :estudios_id"
        try:
            return (await self._ejecutar_comando(query, {"estudios_id": estudios_id})) > 0
        except Exception:
            return False