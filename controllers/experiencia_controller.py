from fastapi import APIRouter, HTTPException, status, Query
from models.experiencia import ExperienciaCreate, ExperienciaUpdate, ExperienciaResponse
from servicios.experiencia_servicio import ExperienciaServicio

router = APIRouter(prefix="/api/experiencia", tags=["experiencia"])

@router.get("/", response_model=list[ExperienciaResponse])
async def listar_experiencias(limite: int = Query(default=1000, ge=1, le=10000)):
    servicio = ExperienciaServicio()
    return await servicio.get_all(limite=limite)

@router.get("/{id}", response_model=ExperienciaResponse)
async def obtener_experiencia(id: int):
    servicio = ExperienciaServicio()
    experiencia = await servicio.get_by_id(id)
    if not experiencia:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")
    return experiencia

@router.post("/", response_model=ExperienciaResponse, status_code=status.HTTP_201_CREATED)
async def crear_experiencia(datos: ExperienciaCreate):
    servicio = ExperienciaServicio()
    nuevo_id = await servicio.create(datos.model_dump())
    
    if nuevo_id:
        return {**datos.model_dump(), "id": nuevo_id}
    
    raise HTTPException(status_code=500, detail="Error al guardar")

@router.put("/{id}", response_model=ExperienciaResponse)
async def actualizar_experiencia(id: int, datos: ExperienciaUpdate):
    servicio = ExperienciaServicio()
    existente = await servicio.get_by_id(id)
    if not existente:
        raise HTTPException(status_code=404, detail="Experiencia no encontrada")

    exito = await servicio.update(id, datos.model_dump())
    if exito:
        return {**datos.model_dump(), "id": id}
    
    raise HTTPException(status_code=500, detail="Error al actualizar")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_experiencia(id: int):
    servicio = ExperienciaServicio()
    exito = await servicio.delete(id)
    if not exito:
        raise HTTPException(status_code=404, detail="No se pudo eliminar")
    return None