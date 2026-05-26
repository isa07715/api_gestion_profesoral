from repositorios.base_repositorio import BaseRepositorioPostgreSQL

class InteresesFuturosRepositorio(BaseRepositorioPostgreSQL):
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._esquema = "public"
        self._tabla = "intereses_futuros"

    async def obtener_todos(self, limite: int = 1000) -> list[dict]:
        query = f"SELECT docente, termino_clave FROM {self._esquema}.{self._tabla} ORDER BY docente LIMIT :limite"
        return await self._ejecutar_query(query, {"limite": limite})

    async def crear(self, datos: dict) -> bool:
        """
        Inserta un nuevo interés.
        Usa ON CONFLICT para evitar duplicados (requiere índice único en DB).
        """
        query = f"""
            INSERT INTO {self._esquema}.{self._tabla} (docente, termino_clave)
            VALUES (:docente, :termino_clave)
            ON CONFLICT (docente, termino_clave) DO NOTHING
        """
        try:
            # ✅ CORRECCIÓN: Usamos 'datos', no 'data'
            filas = await self._ejecutar_comando(query, datos)
            return filas > 0
        except Exception as e:
            print(f"❌ Error Repo Intereses: {e}")
            return False

    async def eliminar(self, cedula: int, termino: str) -> bool:
        query = f"DELETE FROM {self._esquema}.{self._tabla} WHERE docente = :cedula AND termino_clave = :termino"
        try:
            filas = await self._ejecutar_comando(query, {"cedula": cedula, "termino": termino})
            return filas > 0
        except Exception as e:
            print(f"❌ Error Repo Eliminar: {e}")
            return False