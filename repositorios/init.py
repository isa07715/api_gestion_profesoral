"""
repositorios/__init__.py — Inicializa el paquete de repositorios.
"""
from repositorios.area_conocimiento_repositorio import RepositorioAreaConocimientoPostgreSQL
from repositorios.termino_clave_repositorio import RepositorioTerminoClavePostgreSQL
from repositorios.linea_investigacion_repositorio import RepositorioLineaInvestigacionPostgreSQL
from repositorios.programa_repositorio import RepositorioProgramaPostgreSQL
from repositorios.red_repositorio import RepositorioRedPostgreSQL

__all__ = [
    'RepositorioAreaConocimientoPostgreSQL',
    'RepositorioTerminoClavePostgreSQL',
    'RepositorioLineaInvestigacionPostgreSQL',
    'RepositorioProgramaPostgreSQL',
    'RepositorioRedPostgreSQL',
]