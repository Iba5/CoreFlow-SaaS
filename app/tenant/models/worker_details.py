from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from user_details import Base

class Worker_Details(Base):
    __tablename__="WorkerInfo"
    Id = Column(Integer ,ForeignKey("UserInfo.Id"),primary_key=True)
    Leader = Column(String, nullable= True)
    is_active = Column(Boolean,default=True)
    
    # work to user
    worker = relationship("User_Details",uselist=False,back_populates="employee")
