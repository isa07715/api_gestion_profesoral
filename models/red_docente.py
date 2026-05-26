"""
red_docente.py - Modelos Pydantic para la tabla red_docente.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class RedDocenteBase(BaseModel):
    """Esquema base para red_docente."""
    fecha_inicio: date
    fecha_fin: Optional[date] = None
    act_destacadas: str
    red: int
    docente: int


class RedDocenteCreate(RedDocenteBase):
    """Esquema para crear red_docente."""
    pass


class RedDocenteUpdate(BaseModel):
    """Esquema para actualizar red_docente."""
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    act_destacadas: Optional[str] = None
    red: Optional[int] = None
    docente: Optional[int] = None


class RedDocenteResponse(RedDocenteBase):
    """Esquema de respuesta para red_docente."""
    class Config:
        from_attributes = True