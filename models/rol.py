from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class RolBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=500)
    activo: bool = True

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class RolResponse(RolBase):
    id: int
    fecha_creacion: Optional[datetime] = None
    
    # ✅ Configuración correcta para Pydantic v2
    model_config = {"from_attributes": True}