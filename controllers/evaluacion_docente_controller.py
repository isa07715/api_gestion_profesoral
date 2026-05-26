"""
evaluacion_docente_controller.py - Controlador para la tabla evaluacion_docente.
"""
from fastapi import APIRouter, Query, HTTPException
from models.evaluacion_docente import EvaluacionDocenteCreate, EvaluacionDocenteUpdate, EvaluacionDocenteResponse
from servicios.evaluacion_docente_servicio import EvaluacionDocenteServicio

router = APIRouter(prefix="/api/evaluacion_docente", tags=["evaluacion_docente"])


@router.get("/", response_model=list[EvaluacionDocenteResponse])
async def listar_evaluaciones(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todas las evaluaciones de docentes."""
    servicio = EvaluacionDocenteServicio()
    evaluaciones = await servicio.get_all(limite=limite)
    return evaluaciones


@router.get("/{id}", response_model=EvaluacionDocenteResponse)
async def obtener_evaluacion(id: int, esquema: str = Query(default="public")):
    """Obtiene una evaluacion por id."""
    servicio = EvaluacionDocenteServicio()
    evaluacion = await servicio.get_by_id(id)
    
    if evaluacion is None:
        raise HTTPException(status_code=404, detail="Evaluacion no encontrada")
    
    return evaluacion


@router.post("/", status_code=201, response_model=dict)
async def crear_evaluacion(evaluacion: EvaluacionDocenteCreate, esquema: str = Query(default="public")):
    """Crea una nueva evaluacion de docente."""
    servicio = EvaluacionDocenteServicio()
    exito = await servicio.create(evaluacion.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear la evaluacion")
    
    return {"mensaje": "Evaluacion creada exitosamente", "id": evaluacion.docente}


@router.put("/{id}", response_model=dict)
async def actualizar_evaluacion(id: int, evaluacion: EvaluacionDocenteUpdate, esquema: str = Query(default="public")):
    """Actualiza una evaluacion existente."""
    servicio = EvaluacionDocenteServicio()
    exito = await servicio.update(id, evaluacion.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Evaluacion no encontrada")
    
    return {"mensaje": "Evaluacion actualizada exitosamente"}


@router.delete("/{id}", status_code=204)
async def eliminar_evaluacion(id: int, esquema: str = Query(default="public")):
    """Elimina una evaluacion por id."""
    servicio = EvaluacionDocenteServicio()
    exito = await servicio.delete(id)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Evaluacion no encontrada")
    
    return None


@router.get("/docente/{docente}", response_model=list[EvaluacionDocenteResponse])
async def listar_por_docente(docente: int, esquema: str = Query(default="public")):
    """Lista todas las evaluaciones de un docente."""
    servicio = EvaluacionDocenteServicio()
    evaluaciones = await servicio.get_by_docente(docente)
    return evaluaciones