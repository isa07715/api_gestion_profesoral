"""
main.py - Punto de entrada de la API REST con FastAPI.
Proyecto: Gestion Profesoral - Entrega 2
"""
from fastapi import FastAPI
from controllers.area_conocimiento_controller import router as area_conocimiento_router
from controllers.termino_clave_controller import router as termino_clave_router
from controllers.linea_investigacion_controller import router as linea_investigacion_router
from controllers.programa_controller import router as programa_router
from controllers.red_controller import router as red_router
from controllers.docente_controller import router as docente_router
from controllers.estudios_realizados_controller import router as estudios_realizados_router
from controllers.docente_departamento_controller import router as docente_departamento_router 
from controllers.intereses_futuros_controller import router as intereses_futuros_router
from controllers.evaluacion_docente_controller import router as evaluacion_docente_router
from controllers.reconocimiento_controller import router as reconocimiento_router
from controllers.experiencia_controller import router as experiencia_router
from controllers.red_docente_controller import router as red_docente_router
from controllers.estudio_ac_controller import router as estudio_ac_router
from controllers.apoyo_profesoral_controller import router as apoyo_profesoral_router
from controllers.beca_controller import router as beca_router
from controllers.rol_controller import router as rol_router
from controllers.usuario_controller import router as usuario_router
from controllers.rol_usuario_controller import router as rol_usuario_router

app = FastAPI(
    title="API Gestion Profesoral",
    description="API REST CRUD - Entrega 2",
    version="2.0.0",
)

# Registrar controladores
app.include_router(area_conocimiento_router)
app.include_router(termino_clave_router)
app.include_router(linea_investigacion_router)
app.include_router(programa_router)
app.include_router(red_router)
app.include_router(docente_router)
app.include_router(estudios_realizados_router)
app.include_router(docente_departamento_router)
app.include_router(intereses_futuros_router)
app.include_router(evaluacion_docente_router)
app.include_router(reconocimiento_router)
app.include_router(experiencia_router)
app.include_router(red_docente_router) 
app.include_router(estudio_ac_router)
app.include_router(apoyo_profesoral_router)
app.include_router(beca_router) 
app.include_router(rol_router)  
app.include_router(usuario_router)  
app.include_router(rol_usuario_router) 

@app.get("/", tags=["Root"])
async def root():
    return {
        "mensaje": "API Gestion Profesoral - Entrega 2 activa.",
        "documentacion": "/docs",
        "tablas_disponibles": [
            "/api/area_conocimiento",
            "/api/termino_clave",
            "/api/linea_investigacion",
            "/api/programa",
            "/api/red",
            "/api/docente",
            "/api/estudios_realizados",
            "/api/docente_departamento", 
            "/api/intereses_futuros",
            "/api/evaluacion_docente",
            "/api/reconocimiento",
            "/api/experiencia",
            "/api/red_docente",
            "/api/estudio_ac", 
            "/api/apoyo_profesoral",
            "/api/beca",
            "/api/rol",  
            "/api/usuario",  
            "/api/rol_usuario"  
        
        ]

    }