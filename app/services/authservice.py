from fastapi import HTTPException
from sqlalchemy.orm import Session 
from app.tenant.schemas.userAdd import AddUser
from app.repos.authrepo import AuthRepo
from app.tenant.schemas.userAdd import UserResponse,Credentials
from app.core.hashing import HashPassword,VerifyPassword


auth = AuthRepo()
class AuthService:
    def log_in(self,user:str|int,password:str,db:Session):
        """
            Log In Documentation:
        |-> The user here will pass in either an id or username and they will be verified
        |-> We will check if the user exist or not, 
            -> If not we raise an error showing that the user does not exist
        |-> If the user exist we will then validate if the password is the same as the hashed password which would have been returned
            -> If the password does not match we will raise an error showing that the user has entered wrong password
        |-> If all conditions are met then we return the user id since it will be used further
        """
        data = Credentials.model_validate(auth.verify_credentials(user=user,db=db))

        if not data:
            raise HTTPException(status_code=404,detail="User Not Found")
        if not VerifyPassword(password,data.password):
            raise HTTPException(status_code=401,detail="Invalid Password")
        return data.id

    def sign_up(self,user:AddUser,username:str,password:str,db:Session):
        """
            Sign Up documentation
        
        |-> we start by hashing the password 
        |-> we now send it to the repo where details and credentials are all sent
        |-> we check if the adding was a success
        |-> we then return the user details in a pydantic model 
        """
        password = HashPassword(password)
        info = auth.add_details_credentials(user,username,password,db)
        if not info:
            raise HTTPException(
                status_code=500,
                detail="Failed to create user"
            )
        
        return UserResponse(
            id=info["Id"],
            username=info["Username"],
            firstname=info["Firstname"],
            middlename=info["Middlename"],
            lastname=info["Lastname"],
            gender=info["Gender"],
            dob=info["DOB"]
            )
    
    def reset_password(self,user:int|str,password:str,db:Session):
        """
            Reset Password
        |-> We start by verifying if the user exists
        |-> we hash the raw password
        |-> we then update the db with the new password
        |-> we return

            Future Plans
        |-> Add a worker which will be responsible of adding an email to the user to verify if its his plan
        """
        data=auth.verify_credentials(user,db)
        if not data:
            raise HTTPException(status_code=404,detail="User not found")
        pwd = HashPassword(password)
        return auth.update_or_reset_password(data,pwd,db)
    
    def update_password(self,user:int|str,oldpwd:str,password:str,db:Session):
        """
            Update Password
        |-> We start by verifying if the user exists
        |-> We then verify if the old raw password matches with that in db
        |-> we hash the raw password
        |-> we then update the db with the new password
        |-> we return

            Future Plans
        |-> Add a worker which will be responsible of adding an email to the user to verify if its his plan
        """
        data=auth.verify_credentials(user,db)
        if not data:
            raise HTTPException(status_code=404,detail="User not found")
        if not VerifyPassword(oldpwd,data.password):
            raise HTTPException(status_code=401,detail="Invalid Password")
        pwd = HashPassword(password)
        return auth.update_or_reset_password(data,pwd,db)
        