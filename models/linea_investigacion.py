"""
linea_investigacion.py - Modelos Pydantic para la tabla linea_investigacion.
"""
from pydantic import BaseModel, Field


class LineaInvestigacionBase(BaseModel):
    """Esquema base compartido."""
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: str | None = Field(None, max_length=500)


class LineaInvestigacionCreate(LineaInvestigacionBase):
    """Esquema para crear una nueva línea de investigación."""
    pass


class LineaInvestigacionUpdate(LineaInvestigacionBase):
    """Esquema para actualizar una línea de investigación."""
    pass


class LineaInvestigacionResponse(LineaInvestigacionBase):
    """Esquema de respuesta que incluye el ID."""
    id: int
    
    class Config:
        from_attributes = True