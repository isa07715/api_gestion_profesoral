"""
apoyo_profesoral.py - Modelos Pydantic para la tabla apoyo_profesoral.
"""
from pydantic import BaseModel, Field
from typing import Optional


class ApoyoProfesoralBase(BaseModel):
    """Esquema base para apoyo_profesoral."""
    con_apoyo: int
    institucion: str = Field(..., max_length=45)
    tipo: str = Field(..., max_length=45)


class ApoyoProfesoralCreate(ApoyoProfesoralBase):
    """Esquema para crear apoyo_profesoral."""
    estudios: int


class ApoyoProfesoralUpdate(BaseModel):
    """Esquema para actualizar apoyo_profesoral."""
    con_apoyo: Optional[int] = None
    institucion: Optional[str] = Field(None, max_length=45)
    tipo: Optional[str] = Field(None, max_length=45)


class ApoyoProfesoralResponse(ApoyoProfesoralBase):
    """Esquema de respuesta para apoyo_profesoral."""
    estudios: int
    
    class Config:
        from_attributes = True