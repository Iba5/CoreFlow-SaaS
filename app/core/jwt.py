from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm.session import Session
from jose import jwt
from datetime import datetime,timedelta
from app.utils import configs
import secrets
from typing import Any
from uuid import UUID
from RefreshTokenModel import RefreshToken
from hashing import pwd_hash


algo = configs.config.ALGO
secret = configs.config.SECRET

class AccessToken:
    
    def __init__(self) -> None:
        self.refresh= RefreshTokens()

    def login_cookie(self,user:int,role:str,device_id:UUID,db:Session):
        lifetoken = self.refresh.generate_refresh_token(user,device_id,db)
        access = self.generate_new_access_token(user,role,device_id)
        cookie:dict[str,Any]={"access":access,"refresh": lifetoken,"device_id":device_id}
        return cookie
    
    def issue_new_access_token(self,user:int,role:str,db:Session,rawtoken:str,device_id:UUID):
        if self.refresh.validate_refresh_token(device_id,user,rawtoken,db):
            return status.HTTP_401_UNAUTHORIZED
        token = self.generate_new_access_token(user,role,device_id)
        return token

    def generate_new_access_token(self,user_id:int,role:str,device_id:UUID):
        payload:dict[str,Any] = {
            "sub"       : user_id,
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

    def validate_access_token(self,token:str):
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

# class which deals with refresh tokens only
# SOLID principles being implemented
class RefreshTokens:
    # generate a new refresh token
    def generate_refresh_token(self,User_id:int,Device_id:UUID,db:Session):
        token : str = secrets.token_urlsafe(32)
        token_hash=pwd_hash.hash(token)
        refresh:dict[str,Any]={
            "User_id"   : User_id,
            "Device_id" : Device_id,
            "Token"     : token_hash,
            "Iat"       : datetime.now(),
            "Exp"       : datetime.now()+timedelta(days=30),
            "Revoked"   : False    
        }
        
        user=db.query(RefreshToken).filter(
            RefreshToken.User_Id==User_id, 
            RefreshToken.Device_id== Device_id
            ).first()
        
        if user:
            for field, value in refresh.items():
                setattr(user,field,value)

        else: db.add(RefreshToken(**refresh))
        db.commit()
        return token
    
    # validating the refresh token
    def validate_refresh_token(self,device_id:UUID,User_id:int,rawtoken:str,db:Session)->bool:
        user=db.query(RefreshToken).filter(
            RefreshToken.User_Id==User_id, 
            RefreshToken.Device_id== device_id,
            ).first()
        
        #invalid user
        if not user: 
            return True
        
        #expired token
        exp:datetime=getattr(user,"Exp")
        if exp<datetime.now():
            return True
        
        # invalid token
        token= getattr(user,"Token") 
        if not pwd_hash.verify(rawtoken,token):
            return True
        
        return self.is_refresh_revoked(device_id,User_id,db)
       
    #check if the token is revoked
    def is_refresh_revoked(self,device_id:UUID,User:int,db:Session)->bool:
        refresh =db.query(RefreshToken).filter(RefreshToken.User_Id==User, 
                            RefreshToken.Device_id==device_id
                            ).first()
        if not refresh: return True
        data: dict[str,Any] ={
            col.name: getattr(refresh,col.name)
            for col in RefreshToken.__table__.columns
        }
        return data["Revoked"]
    
    #user logs out    
    def revoke_refresh_token(self,device_id:UUID,User:int,db:Session):
        token=db.query(RefreshToken).filter(
                            RefreshToken.User_Id==User, 
                            RefreshToken.Device_id==device_id
                            ).first()
        setattr(token, "Revoked", True)
        db.commit()
        return status.HTTP_200_OK
    
    #user deletes account
    def revoke_all(self,User:int,db:Session):
        data=db.query(RefreshToken).filter(RefreshToken.User_Id==User).all()
        [setattr(d,"Revoked",True) for d in data]
        db.commit()


