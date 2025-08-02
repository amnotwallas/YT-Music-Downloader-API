from pydantic import BaseModel
from typing import List

# This model represents a request to download multiple songs
# It expects a list of song titles or identifiers
class CancionesRequest(BaseModel):
    canciones: List[str]
