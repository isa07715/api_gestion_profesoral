from fastapi import APIRouter, HTTPException, status, Query
from models.beca import BecaCreate, BecaUpdate, BecaResponse
from servicios.beca_servicio import BecaServicio  # ✅ Ahora sí coincide

router = APIRouter(prefix="/api/beca", tags=["beca"])

@router.get("/", response_model=list[BecaResponse])
async def listar_becas(limite: int = Query(default=1000, ge=1, le=10000)):
    servicio = BecaServicio()  # ✅ Uso corregido
    return await servicio.get_all(limite=limite)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def crear_beca(datos: BecaCreate):
    servicio = BecaServicio()
    exito = await servicio.create(datos.model_dump())
    
    if exito:
        return datos.model_dump()
    
    raise HTTPException(status_code=500, detail="Error al guardar")

@router.put("/{estudios_id}", response_model=BecaResponse)
async def actualizar_beca(estudios_id: int, datos: BecaUpdate):
    servicio = BecaServicio()
    exito = await servicio.update(estudios_id, datos.model_dump())
    if exito:
        return {**datos.model_dump(), "estudios": estudios_id}
    raise HTTPException(status_code=500, detail="Error al actualizar")

@router.delete("/{estudios_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_beca(estudios_id: int):
    servicio = BecaServicio()
    exito = await servicio.delete(estudios_id)
    if not exito:
        raise HTTPException(status_code=404, detail="No se pudo eliminar")
    return None