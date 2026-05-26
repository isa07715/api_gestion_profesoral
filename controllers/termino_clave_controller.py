"""
termino_clave_controller.py — Controller para término clave.
"""
from fastapi import APIRouter, HTTPException, Query
from servicios.fabrica_servicios import crear_servicio_termino_clave
from models.termino_clave import TerminoClave, TerminoClaveCreate, TerminoClaveUpdate

router = APIRouter(prefix="/api/termino_clave", tags=["Término Clave"])


@router.get("/", response_model=list[TerminoClave])
async def listar_termino_clave(
    esquema: str = Query(default="public"),
    limite: int = Query(default=1000, ge=1, le=10000)
):
    servicio = crear_servicio_termino_clave()
    try:
        return await servicio.listar(limite=limite)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{termino}", response_model=TerminoClave)
async def obtener_termino_clave(termino: str, esquema: str = Query(default="public")):
    servicio = crear_servicio_termino_clave()
    resultado = await servicio.obtener(termino)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Término clave no encontrado")
    return resultado


@router.post("/", response_model=TerminoClave, status_code=201)
async def crear_termino_clave(datos: TerminoClaveCreate, esquema: str = Query(default="public")):
    servicio = crear_servicio_termino_clave()
    resultado = await servicio.crear(datos.model_dump())
    if resultado is None:
        raise HTTPException(status_code=400, detail="No se pudo crear el término clave")
    return resultado


@router.put("/{termino}", response_model=TerminoClave)
async def actualizar_termino_clave(termino: str, datos: TerminoClaveUpdate, esquema: str = Query(default="public")):
    servicio = crear_servicio_termino_clave()
    datos_dict = {k: v for k, v in datos.model_dump().items() if v is not None}
    resultado = await servicio.actualizar(termino, datos_dict)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Término clave no encontrado")
    return resultado


@router.delete("/{termino}", status_code=204)
async def eliminar_termino_clave(termino: str, esquema: str = Query(default="public")):
    servicio = crear_servicio_termino_clave()
    exito = await servicio.eliminar(termino)
    if not exito:
        raise HTTPException(status_code=404, detail="Término clave no encontrado")
    return None