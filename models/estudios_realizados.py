from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class EstudiosRealizadosBase(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100)
    universidad: str = Field(..., min_length=2, max_length=100)
    fecha: Optional[date] = None  # Acepta YYYY-MM-DD o None
    tipo: str = Field(..., min_length=3, max_length=50)
    ciudad: Optional[str] = None
    pais: Optional[str] = None
    docente: int = Field(..., gt=0, description="Cédula del docente")
    ins_acreditada: int = Field(default=0, description="1=Acreditada, 0=No")
    metodologia: Optional[str] = None
    perfil_egresado: Optional[str] = None  # Agregado para que no de error 422

class EstudiosRealizadosCreate(EstudiosRealizadosBase):
    pass

class EstudiosRealizadosUpdate(EstudiosRealizadosBase):
    pass

class EstudiosRealizadosResponse(EstudiosRealizadosBase):
    id: int

    class Config:
        from_attributes = True