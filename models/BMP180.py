from config.database import Base
from sqlalchemy import Column,Integer,Float,ForeignKey,TIMESTAMP,func
from sqlalchemy.orm import relationship

class BMP180(Base):
    __tablename__ = "BMP180"

    id = Column(Integer, primary_key=True, autoincrement=True)
    presion = Column(Float)
    timestamp = Column(TIMESTAMP, default=func.now())
    limits_id = Column(Integer, ForeignKey('Esp_limits.id'))
    limits = relationship("Esp_limits", back_populates="sensors")
