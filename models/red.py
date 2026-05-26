"""
models/red.py — Modelo Pydantic para red.
Tabla: red (idr, nombre, url, pais)
"""
from pydantic import BaseModel, Field, ConfigDict


class RedBase(BaseModel):
    """Campos base compartidos para crear y actualizar."""
    nombre: str = Field(..., max_length=45, description="Nombre de la red académica")
    url: str = Field(..., max_length=45, description="URL de la red")
    pais: str = Field(..., max_length=45, description="País de origen")


class RedCreate(RedBase):
    """Modelo para crear una nueva red."""
    idr: int = Field(..., description="ID de la red")


class RedUpdate(BaseModel):
    """Modelo para actualizar una red."""
    nombre: str | None = Field(None, max_length=45)
    url: str | None = Field(None, max_length=45)
    pais: str | None = Field(None, max_length=45)


class Red(RedBase):
    """Modelo completo para respuestas de la API."""
    model_config = ConfigDict(from_attributes=True)
    idr: int = Field(..., description="ID de la red académica")
    