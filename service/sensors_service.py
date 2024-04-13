from sqlalchemy.orm import Session
from models.DHT11 import DHT11 
from models.BMP180 import BMP180

def get_all_dht_reads(db: Session):
    return db.query(DHT11).all()

def get_all_bmp_reads(db: Session):
    return db.query(BMP180).all()