"""
programa_controller.py — Controller para programa académico.
"""
from fastapi import APIRouter, HTTPException, Query
from servicios.fabrica_servicios import crear_servicio_programa
from models.programa import Programa, ProgramaCreate, ProgramaUpdate

router = APIRouter(prefix="/api/programa", tags=["Programa"])


@router.get("/", response_model=list[Programa])
async def listar_programa(
    esquema: str = Query(default="public"),
    limite: int = Query(default=1000, ge=1, le=10000)
):
    servicio = crear_servicio_programa()
    try:
        return await servicio.listar(limite=limite)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id}", response_model=Programa)
async def obtener_programa(id: int, esquema: str = Query(default="public")):
    servicio = crear_servicio_programa()
    resultado = await servicio.obtener(id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return resultado


@router.post("/", response_model=Programa, status_code=201)
async def crear_programa(datos: ProgramaCreate, esquema: str = Query(default="public")):
    servicio = crear_servicio_programa()
    resultado = await servicio.crear(datos.model_dump())
    if resultado is None:
        raise HTTPException(status_code=400, detail="No se pudo crear el programa")
    return resultado


@router.put("/{id}", response_model=Programa)
async def actualizar_programa(id: int, datos: ProgramaUpdate, esquema: str = Query(default="public")):
    servicio = crear_servicio_programa()
    datos_dict = {k: v for k, v in datos.model_dump().items() if v is not None}
    resultado = await servicio.actualizar(id, datos_dict)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return resultado


@router.delete("/{id}", status_code=204)
async def eliminar_programa(id: int, esquema: str = Query(default="public")):
    servicio = crear_servicio_programa()
    exito = await servicio.eliminar(id)
    if not exito:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return None