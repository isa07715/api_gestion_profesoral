from repositorios.base_repositorio import BaseRepositorioPostgreSQL

class EstudiosRealizadosRepositorio(BaseRepositorioPostgreSQL):
    def __init__(self, cadena_conexion: str):
        super().__init__(cadena_conexion)
        self._esquema = "public"
        self._tabla = "estudios_realizados"

    async def obtener_todos(self, limite: int = 1000) -> list[dict]:
        query = f"""
            SELECT id, titulo, universidad, fecha, tipo, ciudad, pais, 
                   docente, ins_acreditada, metodologia, perfil_egresado
            FROM {self._esquema}.{self._tabla}
            ORDER BY id
            LIMIT :limite
        """
        return await self._ejecutar_query(query, {"limite": limite})

    async def obtener_por_id(self, id: int) -> dict | None:
        query = f"""
            SELECT id, titulo, universidad, fecha, tipo, ciudad, pais, 
                   docente, ins_acreditada, metodologia, perfil_egresado
            FROM {self._esquema}.{self._tabla}
            WHERE id = :id
        """
        resultados = await self._ejecutar_query(query, {"id": id})
        return resultados[0] if resultados else None

    async def crear(self, datos: dict) -> int | None:
        """
        ✅ CREA un registro y RETORNA el ID generado automáticamente.
        """
        query = f"""
            INSERT INTO {self._esquema}.{self._tabla} 
            (titulo, universidad, fecha, tipo, ciudad, pais, 
             docente, ins_acreditada, metodologia, perfil_egresado)
            VALUES (:titulo, :universidad, :fecha, :tipo, :ciudad, :pais, 
                    :docente, :ins_acreditada, :metodologia, :perfil_egresado)
            RETURNING id
        """
        try:
            # ✅ Usamos _ejecutar_query para leer el resultado (RETURNING id)
            resultado = await self._ejecutar_query(query, datos)
            if resultado:
                return resultado[0]['id']  # Retornamos el ID generado
            return None
        except Exception as e:
            print(f"❌ Error al crear estudio: {e}")
            return None

    async def actualizar(self, id: int, datos: dict) -> bool:
        query = f"""
            UPDATE {self._esquema}.{self._tabla}
            SET titulo = :titulo, universidad = :universidad, fecha = :fecha, 
                tipo = :tipo, ciudad = :ciudad, pais = :pais, 
                docente = :docente, ins_acreditada = :ins_acreditada, 
                metodologia = :metodologia, perfil_egresado = :perfil_egresado
            WHERE id = :id
        """
        datos["id"] = id
        filas = await self._ejecutar_comando(query, datos)
        return filas > 0

    async def eliminar(self, id: int) -> bool:
        query = f"DELETE FROM {self._esquema}.{self._tabla} WHERE id = :id"
        try:
            filas = await self._ejecutar_comando(query, {"id": id})
            return filas > 0
        except Exception as e:
            print(f"❌ Error al eliminar: {e}")
            return False