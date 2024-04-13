from config.database import Base
from sqlalchemy import Column,Integer,Float
from sqlalchemy.orm import relationship

class Ar_limits(Base):
    __tablename__ = "Ar_limits"

    id = Column(Integer,primary_key=True,autoincrement= False)
    temp_limit = Column(Float,default=0)
    hum_limit = Column(Float,default=0)
    sensors = relationship("DHT11",back_populates="Ar_limits")
