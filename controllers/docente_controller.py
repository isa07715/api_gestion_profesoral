"""
docente_controller.py - Controlador para la tabla docente.
"""
from fastapi import APIRouter, Query, HTTPException
from models.docente import DocenteCreate, DocenteUpdate, DocenteResponse
from servicios.docente_servicio import DocenteServicio

router = APIRouter(prefix="/api/docente", tags=["docente"])


@router.get("/", response_model=list[DocenteResponse])
async def listar_docentes(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los docentes."""
    servicio = DocenteServicio()
    docentes = await servicio.get_all(limite=limite)
    return docentes


@router.get("/{cedula}", response_model=DocenteResponse)
async def obtener_docente(cedula: int, esquema: str = Query(default="public")):
    """Obtiene un docente por cedula."""
    servicio = DocenteServicio()
    docente = await servicio.get_by_id(cedula)
    
    if docente is None:
        raise HTTPException(status_code=404, detail="Docente no encontrado")
    
    return docente


@router.post("/", status_code=201, response_model=dict)
async def crear_docente(docente: DocenteCreate, esquema: str = Query(default="public")):
    """Crea un nuevo docente."""
    servicio = DocenteServicio()
    exito = await servicio.create(docente.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el docente")
    
    return {"mensaje": "Docente creado exitosamente", "cedula": docente.cedula}


@router.put("/{cedula}", response_model=dict)
async def actualizar_docente(cedula: int, docente: DocenteUpdate, esquema: str = Query(default="public")):
    """Actualiza un docente existente."""
    servicio = DocenteServicio()
    exito = await servicio.update(cedula, docente.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Docente no encontrado")
    
    return {"mensaje": "Docente actualizado exitosamente"}


@router.delete("/{cedula}", status_code=204)
async def eliminar_docente(cedula: int, esquema: str = Query(default="public")):
    """Elimina un docente por cedula."""
    servicio = DocenteServicio()
    exito = await servicio.delete(cedula)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Docente no encontrado")
    
    return None