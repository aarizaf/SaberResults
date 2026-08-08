from pydantic import BaseModel
from typing import Optional


class ObtenerInfo(BaseModel):
    nombre: str
    grupo: Optional[str] = None

class CrearUsuario(BaseModel):
    usuario: str
    nombre: str
    identificacion: str
    password: Optional[str] = None
    correo: Optional[str] = None



