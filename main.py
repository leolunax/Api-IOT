from fastapi import FastAPI
from fastapi import status
from config.database import Session,engine,Base
from schemes.DHT11_response import DHT11_response
from schemes.BMP180_response import BMP180_response
from schemes.Ar_limits_response import Ar_limits_response
from schemes.Esp_limits_response import Esp_limits_response
from service.limits_service import get_all_ar_limits
from service.limits_service import get_all_esp_limits
from service.sensors_service import get_all_dht_reads
from service.sensors_service import get_all_bmp_reads

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return "Hola Mundo"

@app.get('/ar/limits/',response_model= list[Ar_limits_response])
async def get_limits():
    db = Session()
    limits = get_all_ar_limits(db)
    return limits

@app.get('/esp/limits/',response_model= list[Esp_limits_response])
async def get_limits():
    db = Session()
    limits = get_all_esp_limits(db)
    return limits

#!USO INTERNO, NO USAR PARA FRONTEND
@app.post('/ar/limits/',status_code=status.HTTP_201_CREATED,response_model=Ar_limits_response)
async def limits(limit:Ar_limits_response):
    db=Session()
    from models.Ar_limits import Ar_limits
    new_limit = Ar_limits(
        temp_limit =limit.temp_limit,
        hum_limit = limit.hum_limit,
    ) 
    db.add(new_limit)
    db.commit()
    db.refresh(new_limit)
    return new_limit

#!USO INTERNO, NO USAR PARA FRONTEND
@app.post('/esp/limits/',status_code=status.HTTP_201_CREATED,response_model=Esp_limits_response)
async def limits(limit:Esp_limits_response):
    db=Session()
    from models.Esp_limits import Esp_limits
    new_limit = Esp_limits(
        pres_limit =limit.pres_limit,
    ) 
    db.add(new_limit)
    db.commit()
    db.refresh(new_limit)
    return new_limit


@app.get('/ar/sens/', response_model= list[DHT11_response])
async def get_sensors():
    db = Session()
    sensors = get_all_dht_reads(db)
    return sensors

@app.get('/esp/sens/', response_model= list[BMP180_response])
async def get_sensors():
    db = Session()
    sensors = get_all_bmp_reads(db)
    return sensors


@app.post('/ar/sens/', status_code=status.HTTP_201_CREATED, response_model=DHT11_response)
async def sens(sensor: DHT11_response):
    db = Session()
    from models.DHT11 import DHT11
    new_sensor = DHT11(
        temperature=sensor.temperature,
        humidity=sensor.humidity,
    )
    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)  # Refresca el objeto para obtener el valor del id generado automáticamente
    return new_sensor

@app.post('/esp/sens/', status_code=status.HTTP_201_CREATED, response_model=BMP180_response)
async def sens(sensor: BMP180_response):
    db = Session()
    from models.BMP180 import BMP180
    new_sensor = BMP180(
        presion=sensor.presion,
    )
    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)  # Refresca el objeto para obtener el valor del id generado automáticamente
    return new_sensor

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)