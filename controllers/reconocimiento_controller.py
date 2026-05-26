"""
reconocimiento_controller.py - Controlador para la tabla reconocimiento.
"""
from fastapi import APIRouter, Query, HTTPException
from models.reconocimiento import ReconocimientoCreate, ReconocimientoUpdate, ReconocimientoResponse
from servicios.reconocimiento_servicio import ReconocimientoServicio

router = APIRouter(prefix="/api/reconocimiento", tags=["reconocimiento"])


@router.get("/", response_model=list[ReconocimientoResponse])
async def listar_reconocimientos(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los reconocimientos de docentes."""
    servicio = ReconocimientoServicio()
    reconocimientos = await servicio.get_all(limite=limite)
    return reconocimientos


@router.get("/{id}", response_model=ReconocimientoResponse)
async def obtener_reconocimiento(id: int, esquema: str = Query(default="public")):
    """Obtiene un reconocimiento por id."""
    servicio = ReconocimientoServicio()
    reconocimiento = await servicio.get_by_id(id)
    
    if reconocimiento is None:
        raise HTTPException(status_code=404, detail="Reconocimiento no encontrado")
    
    return reconocimiento


@router.post("/", status_code=201, response_model=dict)
async def crear_reconocimiento(reconocimiento: ReconocimientoCreate, esquema: str = Query(default="public")):
    """Crea un nuevo reconocimiento de docente."""
    servicio = ReconocimientoServicio()
    exito = await servicio.create(reconocimiento.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el reconocimiento")
    
    return {"mensaje": "Reconocimiento creado exitosamente", "id": reconocimiento.docente}


@router.put("/{id}", response_model=dict)
async def actualizar_reconocimiento(id: int, reconocimiento: ReconocimientoUpdate, esquema: str = Query(default="public")):
    """Actualiza un reconocimiento existente."""
    servicio = ReconocimientoServicio()
    exito = await servicio.update(id, reconocimiento.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Reconocimiento no encontrado")
    
    return {"mensaje": "Reconocimiento actualizado exitosamente"}


@router.delete("/{id}", status_code=204)
async def eliminar_reconocimiento(id: int, esquema: str = Query(default="public")):
    """Elimina un reconocimiento por id."""
    servicio = ReconocimientoServicio()
    exito = await servicio.delete(id)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Reconocimiento no encontrado")
    
    return None


@router.get("/docente/{docente}", response_model=list[ReconocimientoResponse])
async def listar_por_docente(docente: int, esquema: str = Query(default="public")):
    """Lista todos los reconocimientos de un docente."""
    servicio = ReconocimientoServicio()
    reconocimientos = await servicio.get_by_docente(docente)
    return reconocimientos