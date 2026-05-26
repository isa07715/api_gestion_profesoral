"""
experiencia.py - Modelos Pydantic para la tabla experiencia.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class ExperienciaBase(BaseModel):
    """Esquema base para experiencia."""
    nombre_cargo: str = Field(..., max_length=45)
    institucion: str = Field(..., max_length=45)
    tipo: str = Field(..., max_length=45)
    fecha_inicio: date
    fecha_fin: Optional[date] = None
    docente: int


class ExperienciaCreate(ExperienciaBase):
    """Esquema para crear experiencia."""
    pass


class ExperienciaUpdate(BaseModel):
    """Esquema para actualizar experiencia."""
    nombre_cargo: Optional[str] = Field(None, max_length=45)
    institucion: Optional[str] = Field(None, max_length=45)
    tipo: Optional[str] = Field(None, max_length=45)
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    docente: Optional[int] = None


class ExperienciaResponse(ExperienciaBase):
    """Esquema de respuesta para experiencia."""
    id: int
    
    class Config:
        from_attributes = True