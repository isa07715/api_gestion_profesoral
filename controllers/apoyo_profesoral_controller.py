from fastapi import APIRouter, HTTPException, status, Query
from models.apoyo_profesoral import ApoyoProfesoralCreate, ApoyoProfesoralUpdate, ApoyoProfesoralResponse
from servicios.apoyo_profesoral_servicio import ApoyoProfesoralServicio

router = APIRouter(prefix="/api/apoyo_profesoral", tags=["apoyo_profesoral"])

@router.get("/", response_model=list[ApoyoProfesoralResponse])
async def listar_apoyos(limite: int = Query(default=1000, ge=1, le=10000)):
    servicio = ApoyoProfesoralServicio()
    return await servicio.get_all(limite=limite)

@router.get("/{estudios_id}", response_model=ApoyoProfesoralResponse)
async def obtener_apoyo(estudios_id: int):
    servicio = ApoyoProfesoralServicio()
    apoyo = await servicio.get_by_estudio(estudios_id)
    if not apoyo:
        raise HTTPException(status_code=404, detail="Apoyo no encontrado para este estudio")
    return apoyo

@router.post("/", status_code=status.HTTP_201_CREATED)
async def crear_apoyo(datos: ApoyoProfesoralCreate):
    servicio = ApoyoProfesoralServicio()
    exito = await servicio.create(datos.model_dump())
    
    if exito:
        return datos.model_dump()
    
    raise HTTPException(status_code=500, detail="Error al guardar")

@router.put("/{estudios_id}", response_model=ApoyoProfesoralResponse)
async def actualizar_apoyo(estudios_id: int, datos: ApoyoProfesoralUpdate):
    servicio = ApoyoProfesoralServicio()
    existente = await servicio.get_by_estudio(estudios_id)
    if not existente:
        raise HTTPException(status_code=404, detail="Apoyo no encontrado")

    exito = await servicio.update(estudios_id, datos.model_dump())
    if exito:
        return {**datos.model_dump(), "estudios": estudios_id}
    
    raise HTTPException(status_code=500, detail="Error al actualizar")

@router.delete("/{estudios_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_apoyo(estudios_id: int):
    servicio = ApoyoProfesoralServicio()
    exito = await servicio.delete(estudios_id)
    if not exito:
        raise HTTPException(status_code=404, detail="No se pudo eliminar")
    return None