"""
servicios/__init__.py — Inicializa el paquete de servicios.
"""
from servicios.area_conocimiento_servicio import ServicioAreaConocimiento
from servicios.termino_clave_servicio import ServicioTerminoClave
from servicios.linea_investigacion_servicio import ServicioLineaInvestigacion
from servicios.programa_servicio import ServicioPrograma
from servicios.red_servicio import ServicioRed

__all__ = [
    'ServicioAreaConocimiento',
    'ServicioTerminoClave',
    'ServicioLineaInvestigacion',
    'ServicioPrograma',
    'ServicioRed',
]