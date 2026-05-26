from fastapi import APIRouter, HTTPException, status, Query
from models.intereses_futuros import InteresesFuturosCreate, InteresesFuturosResponse
from servicios.intereses_futuros_servicio import InteresesFuturosServicio

router = APIRouter(prefix="/api/intereses_futuros", tags=["intereses_futuros"])

@router.get("/", response_model=list[InteresesFuturosResponse])
async def listar_intereses(limite: int = Query(default=1000, ge=1, le=10000)):
    servicio = InteresesFuturosServicio()
    return await servicio.get_all(limite=limite)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def crear_interes(datos: InteresesFuturosCreate):
    servicio = InteresesFuturosServicio()
    
    # ✅ Usamos datos.model_dump()
    exito = await servicio.create(datos.model_dump())
    
    if exito:
        return datos.model_dump()
    
    raise HTTPException(status_code=400, detail="Error al guardar o ya existe")

@router.delete("/{cedula}/{termino}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_interes(cedula: int, termino: str):
    servicio = InteresesFuturosServicio()
    exito = await servicio.delete(cedula, termino)
    if not exito:
        raise HTTPException(status_code=404, detail="No se encontró")
    return None