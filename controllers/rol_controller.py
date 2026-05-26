from fastapi import APIRouter, HTTPException, status, Query
from models.rol import RolCreate, RolUpdate, RolResponse
from servicios.rol_servicio import RolServicio

router = APIRouter(prefix="/api/rol", tags=["rol"])

@router.get("/", response_model=list[RolResponse])
async def listar_roles(limite: int = Query(default=1000, ge=1, le=10000)):
    servicio = RolServicio()
    return await servicio.get_all(limite=limite)

@router.get("/{id}", response_model=RolResponse)
async def obtener_rol(id: int):
    servicio = RolServicio()
    rol = await servicio.get_by_id(id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol

@router.post("/", response_model=RolResponse, status_code=status.HTTP_201_CREATED)
async def crear_rol(datos: RolCreate):
    servicio = RolServicio()
    # Ahora servicio.create devuelve un diccionario {'id': 7, 'fecha_creacion': ...}
    resultado = await servicio.create(datos.model_dump())
    
    if resultado:
        # ✅ Combinamos los datos del input con los datos de la BD (id y fecha)
        return {**datos.model_dump(), **resultado}
    
    raise HTTPException(status_code=500, detail="Error al guardar")

@router.put("/{id}", response_model=RolResponse)
async def actualizar_rol(id: int, datos: RolUpdate):
    servicio = RolServicio()
    existente = await servicio.get_by_id(id)
    if not existente:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    exito = await servicio.update(id, datos.model_dump())
    if exito:
        return {**datos.model_dump(), "id": id}
    
    raise HTTPException(status_code=500, detail="Error al actualizar")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_rol(id: int):
    servicio = RolServicio()
    exito = await servicio.delete(id)
    if not exito:
        raise HTTPException(status_code=404, detail="No se pudo eliminar")
    return None