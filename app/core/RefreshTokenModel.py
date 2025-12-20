from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from app.tenant.models.user_details import Base
from uuid import uuid4

class RefreshToken(Base):
    __tablename__="Tokens"
    Id          =Column(type_=Integer,primary_key=True)
    User_Id     =Column(Integer,ForeignKey("Tenants.Id"))
    Device_id   =Column(PG_UUID(as_uuid=True),unique=True,default=uuid4)
    Token       =Column(String,unique=True)
    Ist         =Column(DateTime)
    Exp         =Column(DateTime)
    Revoked      =Column(Boolean)
