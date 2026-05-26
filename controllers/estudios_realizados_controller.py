from fastapi import APIRouter, HTTPException, status, Query
from models.estudios_realizados import EstudiosRealizadosCreate, EstudiosRealizadosUpdate, EstudiosRealizadosResponse
from servicios.estudios_realizados_servicio import EstudiosRealizadosServicio

router = APIRouter(prefix="/api/estudios_realizados", tags=["estudios_realizados"])

@router.get("/", response_model=list[EstudiosRealizadosResponse])
async def listar_estudios(limite: int = Query(default=1000, ge=1, le=10000)):
    servicio = EstudiosRealizadosServicio()
    return await servicio.get_all(limite=limite)

@router.get("/{id}", response_model=EstudiosRealizadosResponse)
async def obtener_estudio(id: int):
    servicio = EstudiosRealizadosServicio()
    estudio = await servicio.get_by_id(id)
    if not estudio:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")
    return estudio

@router.post("/", response_model=EstudiosRealizadosResponse, status_code=status.HTTP_201_CREATED)
async def crear_estudio(datos: EstudiosRealizadosCreate):
    servicio = EstudiosRealizadosServicio()
    
    # ✅ Recibimos el ID generado desde el repositorio
    nuevo_id = await servicio.create(datos.model_dump())
    
    if nuevo_id:
        # ✅ Retornamos el objeto completo con el ID nuevo
        return {**datos.model_dump(), "id": nuevo_id}
    
    raise HTTPException(status_code=500, detail="Error al guardar en la base de datos")

@router.put("/{id}", response_model=EstudiosRealizadosResponse)
async def actualizar_estudio(id: int, datos: EstudiosRealizadosUpdate):
    servicio = EstudiosRealizadosServicio()
    
    existente = await servicio.get_by_id(id)
    if not existente:
        raise HTTPException(status_code=404, detail="Estudio no encontrado")

    exito = await servicio.update(id, datos.model_dump())
    if exito:
        return {**datos.model_dump(), "id": id}
    
    raise HTTPException(status_code=500, detail="Error al actualizar")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_estudio(id: int):
    servicio = EstudiosRealizadosServicio()
    exito = await servicio.delete(id)
    if not exito:
        raise HTTPException(status_code=404, detail="No se pudo eliminar")
    return None