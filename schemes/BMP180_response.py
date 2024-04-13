from pydantic import BaseModel

class BMP180_response(BaseModel):
    id: int
    presion: float