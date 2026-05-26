"""
models/termino_clave.py — Modelo Pydantic para termino_clave.
Tabla: termino_clave (termino, termino_ingles)
"""
from pydantic import BaseModel, Field, ConfigDict


class TerminoClaveBase(BaseModel):
    """Campos base compartidos para crear y actualizar."""
    termino_ingles: str | None = Field(None, max_length=30, description="Término en inglés")


class TerminoClaveCreate(BaseModel):
    """Modelo para crear un nuevo término clave."""
    termino: str = Field(..., max_length=30, description="Término clave en español")
    termino_ingles: str | None = Field(None, max_length=30)


class TerminoClaveUpdate(BaseModel):
    """Modelo para actualizar un término clave."""
    termino_ingles: str | None = Field(None, max_length=30)


class TerminoClave(BaseModel):
    """Modelo completo para respuestas de la API."""
    model_config = ConfigDict(from_attributes=True)
    termino: str = Field(..., max_length=30, description="Término clave en español")
    termino_ingles: str | None = Field(None, max_length=30)