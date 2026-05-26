"""
docente.py - Modelos Pydantic para la tabla docente.
"""
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import Optional
from datetime import date


class DocenteBase(BaseModel):
    """Esquema base para docente."""
    cedula: int
    nombres: str = Field(..., max_length=60)
    apellidos: str = Field(..., max_length=60)
    genero: str = Field(..., max_length=12)
    cargo: str = Field(..., max_length=30)
    fecha_nacimiento: date
    correo: EmailStr
    telefono: str = Field(..., max_length=20)
    url_cvlac: str = Field(..., max_length=128)
    fecha_actualizacion: date
    escalafon: str = Field(..., max_length=45)
    perfil: str
    cat_minciencia: Optional[str] = Field(None, max_length=45)
    conv_minciencia: str = Field(..., max_length=45)
    
    # ✅ CAMBIO: Usar 'nacionalidaad' con typo para coincidir con la BD
    nacionalidaad: str = Field(..., max_length=45)
    
    linea_investigacion_principal: Optional[int] = None


class DocenteCreate(DocenteBase):
    """Esquema para crear docente."""
    pass


class DocenteUpdate(BaseModel):
    """Esquema para actualizar docente."""
    nombres: Optional[str] = Field(None, max_length=60)
    apellidos: Optional[str] = Field(None, max_length=60)
    genero: Optional[str] = Field(None, max_length=12)
    cargo: Optional[str] = Field(None, max_length=30)
    fecha_nacimiento: Optional[date] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=20)
    url_cvlac: Optional[str] = Field(None, max_length=128)
    fecha_actualizacion: Optional[date] = None
    escalafon: Optional[str] = Field(None, max_length=45)
    perfil: Optional[str] = None
    cat_minciencia: Optional[str] = Field(None, max_length=45)
    conv_minciencia: Optional[str] = Field(None, max_length=45)
    nacionalidaad: Optional[str] = Field(None, max_length=45)  # ✅ Con typo
    linea_investigacion_principal: Optional[int] = None


class DocenteResponse(DocenteBase):
    """Esquema de respuesta para docente."""
    class Config:
        from_attributes = True