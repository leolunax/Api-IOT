from pydantic import BaseModel

class Esp_limits_response(BaseModel):
    id: int
    pres_limit: float