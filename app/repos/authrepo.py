from fastapi import HTTPException
from abc import ABC,abstractmethod
from typing import Any
from sqlalchemy.orm import Session
from app.tenant.schemas.userAdd import AddUser
from app.tenant.models.user_details import User_Details,User_Credentials

class AuthRepository(ABC):
    @abstractmethod
    def add_details_credentials(self,details:AddUser,username:str,password:str,db:Session)->Any:
        pass
    @abstractmethod
    def verify_credentials(self,user:str|int,password:str,db:Session):
        pass
    @abstractmethod
    def update_password(self,user:str|int,password:str,db:Session):
        pass
    @abstractmethod 
    def reset_password(self,user:str|int,password:str,db:Session):
        pass

class AuthRepo(AuthRepository):
    def add_details_credentials(self,details:AddUser,username: str, password: str, db: Session)->Any:
        data = details.model_dump()
        try:
            with db.begin():
                user = User_Details(**data)
                db.add(user)
                db.flush()
                creds= User_Credentials(id=user.Id,username=username,password=password)
                db.add(creds)
                return {
                    "Id":user.Id,
                    "Username":creds.username,
                    "Firstname": user.Firstname,
                    "Lastname": user.Lastname,
                    "DOB":user.DOB,
                    "Gender":user.gender
                }

        except Exception:
            raise HTTPException(
                status_code=500,
                detail="Failed to creat user"
            )


