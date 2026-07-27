from typing import List
from models.result import ObtenerGrupos
from sdk import get_supabase


def obtener_grupos(body: ObtenerGrupos):
    response = (
        get_supabase()
        .table("resultados_nivelacion")
        .select("grupo")
        .eq("grupo", body.grupo)
        .gte("promedio", str(body.promedio))
        .eq("nombre", body.nombre)
        .execute()
    )
    return response["data"]





