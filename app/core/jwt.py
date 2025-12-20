from sqlalchemy.orm.session import Session
from uuid import UUID
from app.tenant.schemas.userAdd import Credentials
from jose import jwt
from datetime import datetime,timedelta
from app.utils import configs
from fastapi import HTTPException,Request
from starlette import status
from RefreshTokenModel import RefreshToken
from typing import Any
from hashing import pwd_hash
import secrets

algo = configs.config.ALGO
secret = configs.config.SECRET

def GenerateToken(user:Credentials,role:str,device_id:UUID):

    payload:dict[str,Any] = {
        "sub"       : user.Id,
        "role"      : role,
        "tenant_id" : " ",
        "device"    : device_id,
        "iat"       :datetime.now(),
        "exp"       : datetime.now()+timedelta(minutes=15),
        "iss"       :"CoreFlow"
    }
    
    return jwt.encode(claims=payload,  #claims
               key=secret,    #signing key
               algorithm=algo #hashing algorrithn
               )

def NewAccessToken(user:Credentials,role:str,db:Session,user_id:int,device_id:UUID):
    if ValidateAccessToken(device_id,user_id,db):
        return status.HTTP_401_UNAUTHORIZED
    token = GenerateToken(user,role,device_id)
    return token

def VerifyAccessToken(token:str):
    try:
        jwt.decode(
                token=token, 
                key=secret,
                algorithms=[algo],
                options={"verify_exp":True}
                )
        return status.HTTP_202_ACCEPTED
    except:
        return HTTPException(status_code=401,detail="Invalid or Expired token")

def ValidateAccessToken(device_id:UUID,User:int,db:Session)->bool:
    refresh =db.query(RefreshToken).filter(RefreshToken.User_Id==User, 
                        RefreshToken.Device_id==device_id
                        ).first()
    if not refresh: return True
    data: dict[str,Any] ={
        col.name: getattr(refresh,col.name)
        for col in RefreshToken.__table__.columns
    }
    return data["Revoked"]


def CreateRefreshToken(request:Request,db:Session):
    token : str = secrets.token_urlsafe(32)
    token=pwd_hash.hash(token)
    refresh:dict[str,Any]={
        "User_id"   : request.headers["User_id"],
        "Device_id" : request.headers["Device_id"],
        "Token"     : token,
        "Ist"       : datetime.now(),
        "Exp"       : datetime.now()+timedelta(days=30),
        "Revoked"   : False    
    }
    
    user=db.query(RefreshToken).filter(
        refresh["User_id"]==RefreshToken.User_Id, 
        refresh["Device_id"]==RefreshToken.Device_id
        ).first()
    
    if user:
        for field, value in refresh.items():
            setattr(user,field,value)

    else: db.add(RefreshToken(**refresh))
    db.commit()
    return status.HTTP_201_CREATED


def RevokeRefreshToken(device_id:UUID,User:int,db:Session):
    token=db.query(RefreshToken).filter(
                        RefreshToken.User_Id==User, 
                        RefreshToken.Device_id==device_id
                        ).first()
    setattr(token, "Revoked", True)
    db.commit()
    return status.HTTP_200_OK


