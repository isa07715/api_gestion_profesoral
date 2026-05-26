from fastapi import APIRouter, HTTPException, status, Query
from models.linea_investigacion import LineaInvestigacionCreate, LineaInvestigacionUpdate, LineaInvestigacionResponse
from servicios.linea_investigacion_servicio import ServicioLineaInvestigacion  # ✅ Nombre corregido

router = APIRouter(prefix="/api/linea_investigacion", tags=["linea_investigacion"])

@router.get("/", response_model=list[LineaInvestigacionResponse])
async def listar_lineas(limite: int = Query(default=1000, ge=1, le=10000)):
    servicio = ServicioLineaInvestigacion()  # ✅ Nombre corregido
    return await servicio.get_all(limite=limite)

@router.get("/{id}", response_model=LineaInvestigacionResponse)
async def obtener_linea(id: int):
    servicio = ServicioLineaInvestigacion()
    linea = await servicio.get_by_id(id)
    if not linea:
        raise HTTPException(status_code=404, detail="Línea no encontrada")
    return linea

@router.post("/", response_model=LineaInvestigacionResponse, status_code=status.HTTP_201_CREATED)
async def crear_linea(datos: LineaInvestigacionCreate):
    servicio = ServicioLineaInvestigacion()
    nuevo_id = await servicio.create(datos.model_dump())
    
    if nuevo_id:
        return {**datos.model_dump(), "id": nuevo_id}
    
    raise HTTPException(status_code=500, detail="Error al guardar")

@router.put("/{id}", response_model=LineaInvestigacionResponse)
async def actualizar_linea(id: int, datos: LineaInvestigacionUpdate):
    servicio = ServicioLineaInvestigacion()
    existente = await servicio.get_by_id(id)
    if not existente:
        raise HTTPException(status_code=404, detail="Línea no encontrada")

    exito = await servicio.update(id, datos.model_dump())
    if exito:
        return {**datos.model_dump(), "id": id}
    
    raise HTTPException(status_code=500, detail="Error al actualizar")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_linea(id: int):
    servicio = ServicioLineaInvestigacion()
    exito = await servicio.delete(id)
    if not exito:
        raise HTTPException(status_code=404, detail="No se pudo eliminar")
    return None