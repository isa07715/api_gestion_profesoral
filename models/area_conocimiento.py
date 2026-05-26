"""
models/area_conocimiento.py — Modelo Pydantic para area_conocimiento.
Tabla: area_conocimiento (id, gran_area, area, disciplina)
"""
from pydantic import BaseModel, Field, ConfigDict


class AreaConocimientoBase(BaseModel):
    """Campos base compartidos para crear y actualizar."""
    gran_area: str = Field(..., max_length=60, description="Gran área del conocimiento")
    area: str = Field(..., max_length=60, description="Área específica del conocimiento")
    disciplina: str = Field(..., max_length=60, description="Disciplina del conocimiento")


class AreaConocimientoCreate(AreaConocimientoBase):
    """Modelo para crear un nuevo área de conocimiento."""
    id: int = Field(..., description="ID del área de conocimiento")


class AreaConocimientoUpdate(BaseModel):
    """Modelo para actualizar un área de conocimiento (todos opcionales)."""
    gran_area: str | None = Field(None, max_length=60)
    area: str | None = Field(None, max_length=60)
    disciplina: str | None = Field(None, max_length=60)


class AreaConocimiento(AreaConocimientoBase):
    """Modelo completo para respuestas de la API."""
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="ID del área de conocimiento")