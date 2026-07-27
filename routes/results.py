from fastapi import APIRouter, HTTPException
from models.result import ObtenerGrupos
from services import result_service
from typing import List
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/SaberResults", tags=["Results"])




@router.post("/obtenerInfoclte")
def obtener_infoclte(body: ObtenerGrupos):
    return result_service.obtener_infoclte(body)

