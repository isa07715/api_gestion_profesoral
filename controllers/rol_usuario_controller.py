"""
rol_usuario_controller.py - Controlador para la tabla rol_usuario.
"""
from fastapi import APIRouter, Query, HTTPException
from models.rol_usuario import RolUsuarioCreate, RolUsuarioResponse
from servicios.rol_usuario_servicio import RolUsuarioServicio

router = APIRouter(prefix="/api/rol_usuario", tags=["rol_usuario"])


@router.get("/", response_model=list[RolUsuarioResponse])
async def listar_roles_usuarios(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los registros de rol_usuario."""
    servicio = RolUsuarioServicio()
    registros = await servicio.get_all(limite=limite)
    return registros


@router.get("/{usuario_id}/{rol_id}", response_model=RolUsuarioResponse)
async def obtener_registro(usuario_id: int, rol_id: int, esquema: str = Query(default="public")):
    """Obtiene un registro por PK compuesta."""
    servicio = RolUsuarioServicio()
    registro = await servicio.get_by_id(usuario_id, rol_id)
    
    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return registro


@router.post("/", status_code=201, response_model=dict)
async def crear_registro(registro: RolUsuarioCreate, esquema: str = Query(default="public")):
    """Crea un nuevo registro en rol_usuario."""
    servicio = RolUsuarioServicio()
    exito = await servicio.create(registro.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el registro")
    
    return {"mensaje": "Registro creado exitosamente", "usuario_id": registro.usuario_id, "rol_id": registro.rol_id}


@router.delete("/{usuario_id}/{rol_id}", status_code=204)
async def eliminar_registro(usuario_id: int, rol_id: int, esquema: str = Query(default="public")):
    """Elimina un registro por PK compuesta."""
    servicio = RolUsuarioServicio()
    exito = await servicio.delete(usuario_id, rol_id)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return None


@router.get("/usuario/{usuario_id}", response_model=list[RolUsuarioResponse])
async def listar_por_usuario(usuario_id: int, esquema: str = Query(default="public")):
    """Lista todos los roles de un usuario."""
    servicio = RolUsuarioServicio()
    registros = await servicio.get_by_usuario(usuario_id)
    return registros


@router.get("/rol/{rol_id}", response_model=list[RolUsuarioResponse])
async def listar_por_rol(rol_id: int, esquema: str = Query(default="public")):
    """Lista todos los usuarios de un rol."""
    servicio = RolUsuarioServicio()
    registros = await servicio.get_by_rol(rol_id)
    return registros