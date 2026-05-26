"""
fabrica_servicios.py — Fábrica para crear servicios.
Implementa el patrón Factory para inyección de dependencias.
"""
from servicios.conexion.proveedor_conexion import get_proveedor_conexion
from servicios.area_conocimiento_servicio import ServicioAreaConocimiento
from servicios.termino_clave_servicio import ServicioTerminoClave
from servicios.linea_investigacion_servicio import ServicioLineaInvestigacion
from servicios.programa_servicio import ServicioPrograma
from servicios.red_servicio import ServicioRed
from repositorios.area_conocimiento_repositorio import RepositorioAreaConocimientoPostgreSQL
from repositorios.termino_clave_repositorio import RepositorioTerminoClavePostgreSQL
from repositorios.linea_investigacion_repositorio import RepositorioLineaInvestigacionPostgreSQL
from repositorios.programa_repositorio import RepositorioProgramaPostgreSQL
from repositorios.red_repositorio import RepositorioRedPostgreSQL


def _obtener_cadena_conexion() -> str:
    """Obtiene la cadena de conexión del proveedor."""
    return get_proveedor_conexion().obtener_cadena_conexion()


def crear_servicio_area_conocimiento() -> ServicioAreaConocimiento:
    """Crea un servicio de área de conocimiento."""
    cadena = _obtener_cadena_conexion()
    repositorio = RepositorioAreaConocimientoPostgreSQL(cadena)
    return ServicioAreaConocimiento(repositorio)


def crear_servicio_termino_clave() -> ServicioTerminoClave:
    """Crea un servicio de término clave."""
    cadena = _obtener_cadena_conexion()
    repositorio = RepositorioTerminoClavePostgreSQL(cadena)
    return ServicioTerminoClave(repositorio)


def crear_servicio_linea_investigacion() -> ServicioLineaInvestigacion:
    """Crea un servicio de línea de investigación."""
    cadena = _obtener_cadena_conexion()
    repositorio = RepositorioLineaInvestigacionPostgreSQL(cadena)
    return ServicioLineaInvestigacion(repositorio)


def crear_servicio_programa() -> ServicioPrograma:
    """Crea un servicio de programa académico."""
    cadena = _obtener_cadena_conexion()
    repositorio = RepositorioProgramaPostgreSQL(cadena)
    return ServicioPrograma(repositorio)


def crear_servicio_red() -> ServicioRed:
    """Crea un servicio de red académica."""
    cadena = _obtener_cadena_conexion()
    repositorio = RepositorioRedPostgreSQL(cadena)
    return ServicioRed(repositorio)