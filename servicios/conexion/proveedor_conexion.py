"""
proveedor_conexion.py - Proveedor de conexiones a base de datos.
"""
from config import get_settings


class ProveedorConexion:
    """Proveedor de conexiones para PostgreSQL."""
    
    def __init__(self):
        self._settings = get_settings()
    
    def obtener_cadena_conexion(self) -> str:
        """Obtiene la cadena de conexión a PostgreSQL con asyncpg."""
        return (
            f"postgresql+asyncpg://"
            f"{self._settings.DB_USER}:{self._settings.DB_PASSWORD}@"
            f"{self._settings.DB_HOST}:{self._settings.DB_PORT}/"
            f"{self._settings.DB_NAME}"
        )
    
    def obtener_proveedor(self) -> str:
        """Obtiene el nombre del proveedor."""
        return "postgresql"
    
    def obtener_host(self) -> str:
        """Obtiene el host."""
        return self._settings.DB_HOST
    
    def obtener_puerto(self) -> int:
        """Obtiene el puerto."""
        return self._settings.DB_PORT
    
    def obtener_base_datos(self) -> str:
        """Obtiene el nombre de la base de datos."""
        return self._settings.DB_NAME


_proveedor = None


def get_proveedor_conexion() -> ProveedorConexion:
    """Obtiene la instancia singleton del proveedor de conexión."""
    global _proveedor
    if _proveedor is None:
        _proveedor = ProveedorConexion()
    return _proveedor