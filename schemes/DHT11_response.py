from pydantic import BaseModel

class DHT11_response(BaseModel):
    id: int
    temperature: float
    humidity: float