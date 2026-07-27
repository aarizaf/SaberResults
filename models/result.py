from pydantic import BaseModel
from typing import Optional


class ObtenerGrupos(BaseModel):
    nombre: str
    grupo: Optional[str] = None
    promedio: float



