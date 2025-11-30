from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import DeclarativeBase,relationship

class Base(DeclarativeBase):
    pass

class User_Details(Base):
    __tablename__="Tenants"
    Id = Column(Integer,primary_key=True)
    Firstname = Column(String,nullable=False)
    Middlename = Column(String,nullable=True)
    Lastname = Column(String ,nullable=False)
    DOB = Column(DateTime,nullable= False)
    gender = Column(String,nullable=True)

    D = relationship("Billing",uselist=True,back_populates="C")
    credentials = relationship("User_Credentials",uselist=False,back_populates="user")

class User_Credentials(Base):
    __tablename__="TenantCredentials"
    id = Column(Integer ,ForeignKey("Tenants.Id",primary_key=True))
    username = Column(String,unique=True)
    password = Column(String,nullable= False)

    user = relationship("User_Details",back_populates="credentials")