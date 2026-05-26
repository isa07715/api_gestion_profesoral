"""
evaluacion_docente.py - Modelos Pydantic para la tabla evaluacion_docente.
"""
from pydantic import BaseModel, Field
from typing import Optional


class EvaluacionDocenteBase(BaseModel):
    """Esquema base para evaluacion_docente."""
    calificacion: float
    semestre: str = Field(..., max_length=45)
    docente: int


class EvaluacionDocenteCreate(EvaluacionDocenteBase):
    """Esquema para crear evaluacion_docente."""
    pass


class EvaluacionDocenteUpdate(BaseModel):
    """Esquema para actualizar evaluacion_docente."""
    calificacion: Optional[float] = None
    semestre: Optional[str] = Field(None, max_length=45)
    docente: Optional[int] = None


class EvaluacionDocenteResponse(EvaluacionDocenteBase):
    """Esquema de respuesta para evaluacion_docente."""
    id: int
    
    class Config:
        from_attributes = True