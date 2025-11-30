from sqlalchemy import Column,String, Integer, Numeric,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from user_details import Base

class Subscriptions(Base):
    __tablename__="Subscriptions"

    Id = Column(Integer,primary_key=True)
    Package = Column(String,unique=True)
    Cost = Column(Numeric(10,2),nullable=False)

    A = relationship("Billing",uselist=True,back_populates="B")

class Billing(Base):
    __tablename__="Bills"

    Id = Column(Integer,primary_key=True)
    PackId = Column(Integer,ForeignKey("Subscriptions.Id"))
    Date= Column(DateTime,default=datetime.now)
    TenantId = Column(Integer,ForeignKey("Tenants.Id"),nullable=False)

    B = relationship("Subscriptions",back_populates="A")
    C = relationship("User_Details",back_populates="D")