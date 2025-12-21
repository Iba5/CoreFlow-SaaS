from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from app.tenant.models.user_details import Base
from uuid import uuid4

class RefreshToken(Base):
    __tablename__="Tokens"
    Id          =Column(type_=Integer,primary_key=True)
    User_Id     =Column(Integer,ForeignKey("UserInfo.Id"))
    Device_id   =Column(PG_UUID(as_uuid=True),default=uuid4)
    Token       =Column(String,unique=True)
    Ist         =Column(DateTime,nullable=False)
    Exp         =Column(DateTime,nullable=False)
    Revoked      =Column(Boolean)

    user = relationship("User_Details",back_populates="tkns")

    __table_args__=(UniqueConstraint("User_Id","Device_Id"))
