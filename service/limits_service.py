from sqlalchemy.orm import Session
from models.Ar_limits import Ar_limits 
from models.Esp_limits import Esp_limits

def get_all_ar_limits(db: Session):
    return db.query(Ar_limits).all()

def get_all_esp_limits(db:Session):
    return db.query(Esp_limits).all()