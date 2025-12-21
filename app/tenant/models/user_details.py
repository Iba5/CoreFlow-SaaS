from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import DeclarativeBase,relationship

class Base(DeclarativeBase):
    pass

class User_Details(Base):
    __tablename__="UserInfo"
    Id = Column(Integer,primary_key=True)
    Firstname = Column(String,nullable=False)
    Middlename = Column(String,nullable=True)
    Lastname = Column(String ,nullable=False)
    DOB = Column(DateTime,nullable= False)
    gender = Column(String,nullable=True)
    
    #Relationships 
    # user and tokens
    tkns=relationship("RefreshToken",back_populates="user",cascade="all, delete-orphan")
    # user to his role
    I = relationship("User_Roles",uselist=False,back_populates="H")
    # accountant to the finances
    accounts = relationship("Payments",uselist=True,back_populates="trans")
    # user to the credentials
    credentials = relationship("User_Credentials",uselist=False,back_populates="user",cascade="all, delete-orphan")
    # user to his work structure
    employee = relationship("Worker_Details",uselist=False,back_populates="worker")

class User_Credentials(Base):
    __tablename__="PersonalInfo"
    id = Column(Integer ,ForeignKey("UserInfo.Id"),primary_key=True)
    username = Column(String,unique=True)
    password = Column(String,nullable= False)

    # credentials to owner
    user = relationship("User_Details",back_populates="credentials")