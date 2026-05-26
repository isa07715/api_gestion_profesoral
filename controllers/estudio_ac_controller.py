"""
estudio_ac_controller.py - Controlador para la tabla estudio_ac.
"""
from fastapi import APIRouter, Query, HTTPException
from models.estudio_ac import EstudioACCreate, EstudioACResponse
from servicios.estudio_ac_servicio import EstudioACServicio

router = APIRouter(prefix="/api/estudio_ac", tags=["estudio_ac"])


@router.get("/", response_model=list[EstudioACResponse])
async def listar_estudio_ac(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los registros de estudio_ac."""
    servicio = EstudioACServicio()
    registros = await servicio.get_all(limite=limite)
    return registros


@router.get("/{estudio}/{area_conocimiento}", response_model=EstudioACResponse)
async def obtener_registro(estudio: int, area_conocimiento: int, esquema: str = Query(default="public")):
    """Obtiene un registro por PK compuesta."""
    servicio = EstudioACServicio()
    registro = await servicio.get_by_id(estudio, area_conocimiento)
    
    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return registro


@router.post("/", status_code=201, response_model=dict)
async def crear_registro(registro: EstudioACCreate, esquema: str = Query(default="public")):
    """Crea un nuevo registro en estudio_ac."""
    servicio = EstudioACServicio()
    exito = await servicio.create(registro.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el registro")
    
    return {"mensaje": "Registro creado exitosamente", "estudio": registro.estudio, "area_conocimiento": registro.area_conocimiento}


@router.delete("/{estudio}/{area_conocimiento}", status_code=204)
async def eliminar_registro(estudio: int, area_conocimiento: int, esquema: str = Query(default="public")):
    """Elimina un registro por PK compuesta."""
    servicio = EstudioACServicio()
    exito = await servicio.delete(estudio, area_conocimiento)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return None


@router.get("/estudio/{estudio}", response_model=list[EstudioACResponse])
async def listar_por_estudio(estudio: int, esquema: str = Query(default="public")):
    """Lista todas las areas de conocimiento de un estudio."""
    servicio = EstudioACServicio()
    registros = await servicio.get_by_estudio(estudio)
    return registros


@router.get("/area/{area_conocimiento}", response_model=list[EstudioACResponse])
async def listar_por_area(area_conocimiento: int, esquema: str = Query(default="public")):
    """Lista todos los estudios de un area de conocimiento."""
    servicio = EstudioACServicio()
    registros = await servicio.get_by_area(area_conocimiento)
    return registros