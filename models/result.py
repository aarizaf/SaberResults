from pydantic import BaseModel
from typing import Optional


class ObtenerInfo(BaseModel):
    nombre: str
    grupo: Optional[str] = None
    



