from pydantic import BaseModel, Field
from datetime import date

class BecaBase(BaseModel):
    estudios: int
    tipo: str | None = None
    institucion: str | None = None
    fecha_inicio: date | None = None
    fecha_fin: date | None = None

class BecaCreate(BecaBase):
    pass

class BecaUpdate(BecaBase):
    pass

class BecaResponse(BecaBase):
    id: int | None = None # Opcional por si acaso
    nombre_estudio: str | None = None
    
    class Config:
        from_attributes = True