"""
rol_usuario.py - Modelos Pydantic para la tabla rol_usuario.
"""
from pydantic import BaseModel


class RolUsuarioBase(BaseModel):
    """Esquema base para rol_usuario."""
    pass


class RolUsuarioCreate(BaseModel):
    """Esquema para crear rol_usuario."""
    usuario_id: int
    rol_id: int


class RolUsuarioUpdate(BaseModel):
    """Esquema para actualizar rol_usuario."""
    pass


class RolUsuarioResponse(BaseModel):
    """Esquema de respuesta para rol_usuario."""
    usuario_id: int
    rol_id: int
    
    class Config:
        from_attributes = True