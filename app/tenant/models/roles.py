from sqlalchemy import Column,String, Integer,ForeignKey
from sqlalchemy.orm import relationship
from user_details import Base


class Roles(Base):
    __tablename__="Roles"
    Id=Column(Integer,primary_key=True)
    Role = Column(String)

    # user_roles and roles
    A = relationship("User_Roles",uselist=True,back_populates="B")
    # roles and endpoints
    E = relationship("Role_Endpoint",uselist=True,back_populates="F")

class User_Roles(Base):
    __tablename__="UserRoles"
    Id = Column(Integer,primary_key=True)
    RoleId= Column(Integer,ForeignKey("Roles.Id"))
    UserId= Column(Integer,ForeignKey("UserInfo.Id"))
    
    #user infor and his role 
    H = relationship("User_Details",back_populates="I")
    # user_role and the type of role
    B = relationship("Roles",back_populates="A")

class Endpoints(Base):
    __tablename__="Endpoints"
    id = Column(Integer,primary_key=True)
    route = Column(String)

    # endpoint and the permission provider
    C=relationship("Role_Endpoint",uselist=True,back_populates="D")

class Role_Endpoint(Base):
    __tablename__="Permission"
    Id=Column(Integer,primary_key=True)
    RoleId=Column(Integer,ForeignKey("Roles.Id"))
    EndpointId=Column(Integer,ForeignKey("Endpoints.Id"))

    #relationship between Permissions to Endpoints
    D = relationship("Endpoints",back_populates="C")
    # relations between Permissions to Roles
    F = relationship("Roles",back_populates="E")

