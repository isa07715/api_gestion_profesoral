"""
red_controller.py — Controller para red académica.
"""
from fastapi import APIRouter, HTTPException, Query
from servicios.fabrica_servicios import crear_servicio_red
from models.red import Red, RedCreate, RedUpdate

router = APIRouter(prefix="/api/red", tags=["Red"])


@router.get("/", response_model=list[Red])
async def listar_red(
    esquema: str = Query(default="public"),
    limite: int = Query(default=1000, ge=1, le=10000)
):
    servicio = crear_servicio_red()
    try:
        return await servicio.listar(limite=limite)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{idr}", response_model=Red)
async def obtener_red(idr: int, esquema: str = Query(default="public")):
    servicio = crear_servicio_red()
    resultado = await servicio.obtener(idr)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Red no encontrada")
    return resultado


@router.post("/", response_model=Red, status_code=201)
async def crear_red(datos: RedCreate, esquema: str = Query(default="public")):
    servicio = crear_servicio_red()
    resultado = await servicio.crear(datos.model_dump())
    if resultado is None:
        raise HTTPException(status_code=400, detail="No se pudo crear la red")
    return resultado


@router.put("/{idr}", response_model=Red)
async def actualizar_red(idr: int, datos: RedUpdate, esquema: str = Query(default="public")):
    servicio = crear_servicio_red()
    datos_dict = {k: v for k, v in datos.model_dump().items() if v is not None}
    resultado = await servicio.actualizar(idr, datos_dict)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Red no encontrada")
    return resultado


@router.delete("/{idr}", status_code=204)
async def eliminar_red(idr: int, esquema: str = Query(default="public")):
    servicio = crear_servicio_red()
    exito = await servicio.eliminar(idr)
    if not exito:
        raise HTTPException(status_code=404, detail="Red no encontrada")
    return None
