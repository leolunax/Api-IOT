from config.database import Base
from sqlalchemy import Column,Integer,Float,ForeignKey,TIMESTAMP,func
from sqlalchemy.orm import relationship

class DHT11(Base):
    __tablename__ = "DHT11"

    id = Column(Integer,primary_key=True,autoincrement= True)
    temperature = Column(Float)
    humidity = Column(Float)
    timestamp = Column(TIMESTAMP,default=func.now())
    limits_id = Column(Integer,ForeignKey('Ar_limits.id'))
    limits = relationship("Ar_limits",back_populates="DHT11")