"""
estudio_ac.py - Modelos Pydantic para la tabla estudio_ac.
"""
from pydantic import BaseModel, Field


class EstudioACBase(BaseModel):
    """Esquema base para estudio_ac."""
    pass


class EstudioACCreate(BaseModel):
    """Esquema para crear estudio_ac."""
    estudio: int
    area_conocimiento: int


class EstudioACUpdate(BaseModel):
    """Esquema para actualizar estudio_ac."""
    # No hay campos actualizables, solo la PK compuesta
    pass


class EstudioACResponse(BaseModel):
    """Esquema de respuesta para estudio_ac."""
    estudio: int
    area_conocimiento: int
    
    class Config:
        from_attributes = True