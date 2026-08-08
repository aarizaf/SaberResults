from fastapi import APIRouter, HTTPException
from models.humboldt_models import CrearUsuario
from services import humboldt_service
from typing import List
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/SaberResults", tags=["Resultados"])




@router.post("/crearProfesor")
def crear_usuario(body: CrearUsuario):
    try:
        data = humboldt_service.crearProfesor(body)
        if data is None:
            return JSONResponse(
                content={"success": False, "detail": "No se pudo crear el usuario. El usuario ya existe en la base de datos."}, status_code=404)
        return JSONResponse(content={"success": True, "info_clte": data}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"success": False, "detail": str(e)}, status_code=500)






