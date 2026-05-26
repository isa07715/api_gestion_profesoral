# API Gestión Profesoral - Entrega 2

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

## 📋 Descripción

API RESTful desarrollada con **FastAPI** implementando arquitectura de 3 capas (Presentación, Negocio, Datos) para el módulo **Gestión Profesoral** de la Universidad.

- **Entrega 1:** CRUD para 5 tablas sin claves foráneas ✅
- **Entrega 2:** CRUD para tablas adicionales con referencia a docente 🔄

## 📊 Tablas Implementadas

### Entrega 1 - Módulo Gestión Profesoral

| # | Tabla | PK | Endpoints | Estado |
|---|-------|-----|-----------|--------|
| 1 | `area_conocimiento` | id | `/api/area_conocimiento` | ✅ |
| 2 | `termino_clave` | termino | `/api/termino_clave` | ✅ |
| 3 | `linea_investigacion` | id (SERIAL) | `/api/linea_investigacion` | ✅ |
| 4 | `programa` | id | `/api/programa` | ✅ |
| 5 | `red` | idr | `/api/red` | ✅ |

### Entrega 2 - Módulo Docentes
6. `docente` - Información completa del perfil profesoral
7. `estudios_realizados` - Estudios académicos de cada docente
8. `docente_departamento` - Vinculación docente a programas
9. `intereses_futuros` - Intereses de investigación futuros
10. `evaluacion_docente` - Evaluaciones de desempeño por semestre
11. `reconocimiento` - Reconocimientos y premios obtenidos
12. `experiencia` - Experiencia laboral/profesional
13. `red_docente` - Participación en redes académicas
14. `estudio_ac` - Relación estudios-áreas de conocimiento
15. `apoyo_profesoral` - Apoyos institucionales para estudios
16. `beca` - Becas otorgadas a docentes

#### Gestión de Usuarios (3 tablas)
17. `rol` - Roles del sistema (admin, editor, consulta)
18. `usuario` - Usuarios con credenciales de acceso
19. `rol_usuario` - Relación muchos-a-muchos usuario-rol

