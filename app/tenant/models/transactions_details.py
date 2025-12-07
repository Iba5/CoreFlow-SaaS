from sqlalchemy import Column,String, Integer, Numeric, Enum,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.tenant.schemas.transactions import Status
from user_details import Base

class Payments(Base):
    __tablename__="Transactions"
    
    id = Column(Integer, primary_key=True)
    Description= Column(String,nullable=False)
    Amount= Column(Numeric(10,2),nullable=False)
    Type=Column(Enum(Status))
    Date=Column(DateTime,default=datetime.now)
    user_Id = Column(Integer ,ForeignKey("UserInfo.Id"))

    # finances to user
    trans= relationship("User_Details",back_populates="accounts")
