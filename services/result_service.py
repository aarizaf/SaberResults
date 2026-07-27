from typing import List
from models.result import ObtenerInfo
from sdk import supabase


def obtener_infoclte(body: ObtenerInfo):
    response = (
        supabase()
        .table("resultados_nivelacion")
        .select("grupo", "promedio")
        .eq("nombre", body.nombre)
        .execute()
    )
    return response["data"]





