"""
reconocimiento.py - Modelos Pydantic para la tabla reconocimiento.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class ReconocimientoBase(BaseModel):
    """Esquema base para reconocimiento."""
    tipo: str = Field(..., max_length=45)
    fecha: date
    institucion: str = Field(..., max_length=45)
    nombre: str = Field(..., max_length=45)
    ambito: str = Field(..., max_length=45)
    docente: int


class ReconocimientoCreate(ReconocimientoBase):
    """Esquema para crear reconocimiento."""
    pass


class ReconocimientoUpdate(BaseModel):
    """Esquema para actualizar reconocimiento."""
    tipo: Optional[str] = Field(None, max_length=45)
    fecha: Optional[date] = None
    institucion: Optional[str] = Field(None, max_length=45)
    nombre: Optional[str] = Field(None, max_length=45)
    ambito: Optional[str] = Field(None, max_length=45)
    docente: Optional[int] = None


class ReconocimientoResponse(ReconocimientoBase):
    """Esquema de respuesta para reconocimiento."""
    id: int
    
    class Config:
        from_attributes = True