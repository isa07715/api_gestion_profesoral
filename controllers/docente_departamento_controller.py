"""
docente_departamento_controller.py - Controlador para la tabla docente_departamento.
"""
from fastapi import APIRouter, Query, HTTPException
from models.docente_departamento import DocenteDepartamentoCreate, DocenteDepartamentoUpdate, DocenteDepartamentoResponse
from servicios.docente_departamento_servicio import DocenteDepartamentoServicio

router = APIRouter(prefix="/api/docente_departamento", tags=["docente_departamento"])


@router.get("/", response_model=list[DocenteDepartamentoResponse])
async def listar_docente_departamento(esquema: str = Query(default="public"), limite: int = Query(default=1000)):
    """Lista todos los registros de docente_departamento."""
    servicio = DocenteDepartamentoServicio()
    registros = await servicio.get_all(limite=limite)
    return registros


@router.get("/{docente}/{departamento}", response_model=DocenteDepartamentoResponse)
async def obtener_registro(docente: int, departamento: int, esquema: str = Query(default="public")):
    """Obtiene un registro por PK compuesta."""
    servicio = DocenteDepartamentoServicio()
    registro = await servicio.get_by_id(docente, departamento)
    
    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return registro


@router.post("/", status_code=201, response_model=dict)
async def crear_registro(registro: DocenteDepartamentoCreate, esquema: str = Query(default="public")):
    """Crea un nuevo registro en docente_departamento."""
    servicio = DocenteDepartamentoServicio()
    exito = await servicio.create(registro.model_dump())
    
    if not exito:
        raise HTTPException(status_code=400, detail="Error al crear el registro")
    
    return {"mensaje": "Registro creado exitosamente", "docente": registro.docente, "departamento": registro.departamento}


@router.put("/{docente}/{departamento}", response_model=dict)
async def actualizar_registro(docente: int, departamento: int, registro: DocenteDepartamentoUpdate, esquema: str = Query(default="public")):
    """Actualiza un registro existente."""
    servicio = DocenteDepartamentoServicio()
    exito = await servicio.update(docente, departamento, registro.model_dump(exclude_unset=True))
    
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return {"mensaje": "Registro actualizado exitosamente"}


@router.delete("/{docente}/{departamento}", status_code=204)
async def eliminar_registro(docente: int, departamento: int, esquema: str = Query(default="public")):
    """Elimina un registro por PK compuesta."""
    servicio = DocenteDepartamentoServicio()
    exito = await servicio.delete(docente, departamento)
    
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    return None