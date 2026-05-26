"""
models/__init__.py — Inicializa el paquete de modelos Pydantic.
"""
from models.area_conocimiento import AreaConocimiento, AreaConocimientoCreate, AreaConocimientoUpdate
from models.termino_clave import TerminoClave, TerminoClaveCreate, TerminoClaveUpdate
from models.linea_investigacion import LineaInvestigacion, LineaInvestigacionCreate, LineaInvestigacionUpdate
from models.programa import Programa, ProgramaCreate, ProgramaUpdate
from models.red import Red, RedCreate, RedUpdate

__all__ = [
    'AreaConocimiento', 'AreaConocimientoCreate', 'AreaConocimientoUpdate',
    'TerminoClave', 'TerminoClaveCreate', 'TerminoClaveUpdate',
    'LineaInvestigacion', 'LineaInvestigacionCreate', 'LineaInvestigacionUpdate',
    'Programa', 'ProgramaCreate', 'ProgramaUpdate',
    'Red', 'RedCreate', 'RedUpdate',
]
