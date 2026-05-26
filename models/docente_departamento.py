"""
docente_departamento.py - Modelos Pydantic para la tabla docente_departamento.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class DocenteDepartamentoBase(BaseModel):
    """Esquema base para docente_departamento."""
    dedicacion: str = Field(..., max_length=15)
    modalidad: str = Field(..., max_length=45)
    fecha_ingreso: date
    fecha_salida: Optional[date] = None


class DocenteDepartamentoCreate(DocenteDepartamentoBase):
    """Esquema para crear docente_departamento."""
    docente: int
    departamento: int


class DocenteDepartamentoUpdate(BaseModel):
    """Esquema para actualizar docente_departamento."""
    dedicacion: Optional[str] = Field(None, max_length=15)
    modalidad: Optional[str] = Field(None, max_length=45)
    fecha_ingreso: Optional[date] = None
    fecha_salida: Optional[date] = None


class DocenteDepartamentoResponse(DocenteDepartamentoBase):
    """Esquema de respuesta para docente_departamento."""
    docente: int
    departamento: int
    
    class Config:
        from_attributes = True