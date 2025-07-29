from pydantic import BaseModel
from typing import List

class CancionesRequest(BaseModel):
    canciones: List[str]
