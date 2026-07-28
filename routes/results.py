from fastapi import APIRouter, HTTPException
from models.result import ObtenerInfo
from services import result_service
from typing import List
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/SaberResults", tags=["Resultados"])




@router.post("/obtenerInfoclte")
def obtener_infoclte(body: ObtenerInfo):
    data = result_service.obtener_infoclte(body)
    if not data:
        raise HTTPException(status_code=404, detail="No se encontraron resultados para el nombre especificado.")
    return JSONResponse(content={"info_clte": data})


@router.post("/obtenerGrupos")
def obtener_grupos(body: ObtenerInfo):
    grupos = result_service.obtener_grupos(body)
    if not grupos:
        raise HTTPException(status_code=404, detail="No se encontraron resultados para el grupo especificado.")
    return JSONResponse(content={"grupos": grupos})

