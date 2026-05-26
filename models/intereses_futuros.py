"""
intereses_futuros.py - Modelos Pydantic para la tabla intereses_futuros.
"""
from pydantic import BaseModel, Field


class InteresesFuturosBase(BaseModel):
    """Esquema base para intereses_futuros."""
    pass


class InteresesFuturosCreate(BaseModel):
    """Esquema para crear intereses_futuros."""
    docente: int
    termino_clave: str = Field(..., max_length=100)


class InteresesFuturosUpdate(BaseModel):
    """Esquema para actualizar intereses_futuros."""
    # No hay campos actualizables, solo la PK compuesta
    pass


class InteresesFuturosResponse(BaseModel):
    """Esquema de respuesta para intereses_futuros."""
    docente: int
    termino_clave: str
    
    class Config:
        from_attributes = True