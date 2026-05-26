from fastapi import APIRouter, HTTPException, status, Query
from models.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from servicios.usuario_servicio import UsuarioServicio

router = APIRouter(prefix="/api/usuario", tags=["usuario"])

@router.get("/", response_model=list[UsuarioResponse])
async def listar_usuarios(limite: int = Query(default=1000, ge=1, le=10000)):
    servicio = UsuarioServicio()
    return await servicio.get_all(limite=limite)

@router.get("/{id}", response_model=UsuarioResponse)
async def obtener_usuario(id: int):
    servicio = UsuarioServicio()
    usuario = await servicio.get_by_id(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def crear_usuario(datos: UsuarioCreate):
    servicio = UsuarioServicio()
    # ✅ Convertimos el modelo a diccionario y lo pasamos
    resultado = await servicio.create(datos.model_dump())
    
    if resultado:
        return {**datos.model_dump(), **resultado}
    
    raise HTTPException(status_code=500, detail="Error al guardar")

@router.put("/{id}", response_model=UsuarioResponse)
async def actualizar_usuario(id: int, datos: UsuarioUpdate):
    servicio = UsuarioServicio()
    existente = await servicio.get_by_id(id)
    if not existente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    exito = await servicio.update(id, datos.model_dump())
    if exito:
        return {**datos.model_dump(), "id": id}
    
    raise HTTPException(status_code=500, detail="Error al actualizar")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_usuario(id: int):
    servicio = UsuarioServicio()
    exito = await servicio.delete(id)
    if not exito:
        raise HTTPException(status_code=404, detail="No se pudo eliminar")
    return None