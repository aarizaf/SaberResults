from typing import List
from models.humboldt_models import ObtenerInfo, CrearUsuario
from sdk import supabase



def crearUsuario(body: CrearUsuario):
    if body.usuario=="profesor":
        tabla = "profesor_enc"
    elif body.usuario=="estudiante":
        tabla = "estudiante_enc"
    else:
        return None

    existe_usuario = (
        supabase()
        .table(tabla)
        .select("*")
        .eq("nombre", body.nombre)
        .execute()
    )

    if existe_usuario["data"]:
        print("El usuario ya existe en la base de datos.")
        return None
    else:
        nuevo_usuario = {
            "nombre": body.nombre,
            "identificacion": body.identificacion,
            "correo": body.correo,
            "password": body.password
        }
        response = supabase().table(tabla).insert(nuevo_usuario).execute()
        return response["data"]








