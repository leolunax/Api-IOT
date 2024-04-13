from pydantic import BaseModel

class Ar_limits_response(BaseModel):
    id: int
    temp_limit: float
    hum_limit: float