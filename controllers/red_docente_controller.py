"""
red_docente_controller.py - Controlador para la tabla red_docente.
"""
from fastapi import APIRouter, Query, HTTPException
from models.red_docente import RedDocenteCreate, RedDocenteUpdate, RedDocenteResponse
from servicios.red_docente_servicio import RedDocenteServicio

router = APIRouter(prefix="/api/red_docente", tags=["red_docente"])


@router.get("/", response_model=list[RedDocenteResponse])
async def listar_red_docente(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los registros de red_docente."""
    servicio = RedDocenteServicio()
    registros = await servicio.get_all(limite=limite)
    return registros


@router.get("/{red}/{docente}", response_model=RedDocenteResponse)
async def obtener_registro(red: int, docente: int, esquema: str = Query(default="public")):
    """Obtiene un registro por PK compuesta."""
    servicio = RedDocenteServicio()
    registro = await servicio.get_by_id(red, docente)
    
    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return registro


@router.post("/", status_code=201, response_model=dict)
async def crear_registro(registro: RedDocenteCreate, esquema: str = Query(default="public")):
    """Crea un nuevo registro en red_docente."""
    servicio = RedDocenteServicio()
    exito = await servicio.create(registro.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el registro")
    
    return {"mensaje": "Registro creado exitosamente", "red": registro.red, "docente": registro.docente}


@router.put("/{red}/{docente}", response_model=dict)
async def actualizar_registro(red: int, docente: int, registro: RedDocenteUpdate, esquema: str = Query(default="public")):
    """Actualiza un registro existente."""
    servicio = RedDocenteServicio()
    exito = await servicio.update(red, docente, registro.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return {"mensaje": "Registro actualizado exitosamente"}


@router.delete("/{red}/{docente}", status_code=204)
async def eliminar_registro(red: int, docente: int, esquema: str = Query(default="public")):
    """Elimina un registro por PK compuesta."""
    servicio = RedDocenteServicio()
    exito = await servicio.delete(red, docente)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return None


@router.get("/docente/{docente}", response_model=list[RedDocenteResponse])
async def listar_por_docente(docente: int, esquema: str = Query(default="public")):
    """Lista todas las redes de un docente."""
    servicio = RedDocenteServicio()
    registros = await servicio.get_by_docente(docente)
    return registros


@router.get("/red/{red}", response_model=list[RedDocenteResponse])
async def listar_por_red(red: int, esquema: str = Query(default="public")):
    """Lista todos los docentes de una red."""
    servicio = RedDocenteServicio()
    registros = await servicio.get_by_red(red)
    return registros