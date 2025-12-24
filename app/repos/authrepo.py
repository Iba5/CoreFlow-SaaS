from fastapi import HTTPException
from abc import ABC,abstractmethod
from typing import Any
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.core.RefreshTokenModel import RefreshToken
from app.tenant.schemas.userAdd import AddUser
from app.tenant.models.user_details import User_Details,User_Credentials

class AuthRepository(ABC):
    @abstractmethod
    def add_details_credentials(self,details:AddUser,username:str,password:str,db:Session)->Any:
        pass
    @abstractmethod
    def verify_credentials(self,user:str|int,db:Session)->Any:
        pass
    @abstractmethod
    def update_or_reset_password(self,user:User_Credentials,pwd:str,db:Session)->Any:
        pass
    @abstractmethod 
    def reset_password(self,user:str|int,password:str,db:Session):
        pass

class AuthRepo(AuthRepository):
    def add_details_credentials(self,details:AddUser,username: str, password: str, db: Session)->Any:
        """
        Docstring for add_details_credentials
        
        |-> We will start by creating a transaction
        |-> We will convert the User Details Pydantic Schemas to a dict
        |-> We use that dict to add the details into the Db
        |-> We then temporarily store but not commit so that the Id is generated
        |-> We obtain that Id and we then use it as a Foreign key to the Credentials table which will be storing
        |   1. User Id
        |   2. Username
        |   3. Hashed Password
        |-> So after this transaction is complete it automatically commits the data to the db
        |-> Else it will rollback to the initial point the thorw an exception
        """
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
        
    def verify_credentials(self, user: str | int, db: Session)->Any:
        """
        Docstring for verify_credentials
        
        |-> Here we will pass in the user inform of id or string(username)
        |-> So we write a query which will check if the user exists by checking for 2 cases 
        |   1. matching Id
        |   2. matching username
        |-> And we will return the result to the business service and the result will be either
        |   1. user information
        |   2. None
        """
        return db.query(User_Credentials).filter(
            or_(
                User_Credentials.id==user,User_Credentials.username==user
                )
            ).first()
    
    def update_or_reset_password(self, user:User_Credentials,pwd:str, db: Session)->Any:
        """
        |-> Here I will take the Credentials which would have been passed by the service layer
        |-> I will take the new hashed password and I will then overwrite to that old one
        |-> I will commit and refresh the DB to permanently save in the DB
        |-> I will take the user Id and filter all of his active refresh tokens and revoke them
        |   this will result in the other devices being logged out 
        """
        setattr(user,"password",pwd)
        db.commit()
        db.refresh(user) 
        userid = user.id
        db.query(RefreshToken).filter(
            RefreshToken.User_Id==userid
            ).update(
                {RefreshToken.Revoked:True},
                synchronize_session=False
            )
        db.commit()      
        return user
        
            

