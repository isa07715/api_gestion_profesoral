from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)
    email: Optional[EmailStr] = None
    nombre_completo: str = Field(..., max_length=100)
    activo: bool = True

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    password: Optional[str] = Field(None, min_length=6)

class UsuarioResponse(UsuarioBase):
    id: int
    fecha_creacion: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None
    
    # ✅ Configuración para Pydantic v2
    model_config = {"from_attributes": True}