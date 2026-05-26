"""
models/programa.py — Modelo Pydantic para programa.
Tabla: programa (id, nombre, tipo, nivel, fechas, ciudad, facultad)
"""
from pydantic import BaseModel, Field, ConfigDict


class ProgramaBase(BaseModel):
    """Campos base compartidos para crear y actualizar."""
    nombre: str = Field(..., max_length=60, description="Nombre del programa académico")
    tipo: str = Field(..., max_length=45, description="Tipo de programa")
    nivel: str = Field(..., max_length=45, description="Nivel académico")
    fecha_creacion: str = Field(..., max_length=45, description="Fecha de creación")
    fecha_cierre: str | None = Field(None, max_length=45, description="Fecha de cierre")
    numero_cohortes: str = Field(..., max_length=45, description="Número de cohortes")
    cant_graduados: str = Field(..., max_length=45, description="Cantidad de graduados")
    fecha_actualizacion: str = Field(..., max_length=45, description="Fecha de actualización")
    ciudad: str = Field(..., max_length=45, description="Ciudad del programa")
    facultad: int = Field(..., description="ID de la facultad")


class ProgramaCreate(ProgramaBase):
    """Modelo para crear un nuevo programa."""
    id: int = Field(..., description="ID del programa")


class ProgramaUpdate(BaseModel):
    """Modelo para actualizar un programa."""
    nombre: str | None = Field(None, max_length=60)
    tipo: str | None = Field(None, max_length=45)
    nivel: str | None = Field(None, max_length=45)
    fecha_creacion: str | None = Field(None, max_length=45)
    fecha_cierre: str | None = Field(None, max_length=45)
    numero_cohortes: str | None = Field(None, max_length=45)
    cant_graduados: str | None = Field(None, max_length=45)
    fecha_actualizacion: str | None = Field(None, max_length=45)
    ciudad: str | None = Field(None, max_length=45)
    facultad: int | None = None


class Programa(ProgramaBase):
    """Modelo completo para respuestas de la API."""
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., description="ID del programa académico")