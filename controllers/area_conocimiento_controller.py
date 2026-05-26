"""
area_conocimiento_controller.py — Controller para área de conocimiento.
Capa de presentación: maneja rutas HTTP y respuestas JSON.
"""
from fastapi import APIRouter, HTTPException, Query
from servicios.fabrica_servicios import crear_servicio_area_conocimiento
from models.area_conocimiento import AreaConocimiento, AreaConocimientoCreate, AreaConocimientoUpdate
from typing import Any

router = APIRouter(prefix="/api/area_conocimiento", tags=["Área Conocimiento"])


@router.get("/", response_model=list[AreaConocimiento])
async def listar_area_conocimiento(
    esquema: str = Query(default="public", description="Esquema de la base de datos"),
    limite: int = Query(default=1000, ge=1, le=10000, description="Límite de resultados")
):
    """Lista todas las áreas de conocimiento."""
    servicio = crear_servicio_area_conocimiento()
    try:
        resultados = await servicio.listar(limite=limite)
        return resultados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id}", response_model=AreaConocimiento)
async def obtener_area_conocimiento(id: int, esquema: str = Query(default="public")):
    """Obtiene un área de conocimiento por ID."""
    servicio = crear_servicio_area_conocimiento()
    resultado = await servicio.obtener(id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Área de conocimiento no encontrada")
    return resultado


@router.post("/", response_model=AreaConocimiento, status_code=201)
async def crear_area_conocimiento(datos: AreaConocimientoCreate, esquema: str = Query(default="public")):
    """Crea un nuevo área de conocimiento."""
    servicio = crear_servicio_area_conocimiento()
    resultado = await servicio.crear(datos.model_dump())
    if resultado is None:
        raise HTTPException(status_code=400, detail="No se pudo crear el área de conocimiento")
    return resultado


@router.put("/{id}", response_model=AreaConocimiento)
async def actualizar_area_conocimiento(id: int, datos: AreaConocimientoUpdate, esquema: str = Query(default="public")):
    """Actualiza un área de conocimiento existente."""
    servicio = crear_servicio_area_conocimiento()
    datos_dict = {k: v for k, v in datos.model_dump().items() if v is not None}
    resultado = await servicio.actualizar(id, datos_dict)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Área de conocimiento no encontrada")
    return resultado


@router.delete("/{id}", status_code=204)
async def eliminar_area_conocimiento(id: int, esquema: str = Query(default="public")):
    """Elimina un área de conocimiento."""
    servicio = crear_servicio_area_conocimiento()
    exito = await servicio.eliminar(id)
    if not exito:
        raise HTTPException(status_code=404, detail="Área de conocimiento no encontrada")
    return None