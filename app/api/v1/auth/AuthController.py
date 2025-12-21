from fastapi import APIRouter,HTTPException
from starlette.requests import Request
from tenant.schemas.userAdd import Credentials,ResetCredentials,UpdateCredentials,AddUser
from app.services.authservice import AuthService
from app.core.hashing import HashPassword, VerifyPassword


sec=AuthService()

class AuthController:
    auth = APIRouter(prefix="/auth",tags=["Authentication"])

    @auth.post("/signin")
    async def SignIn(self,userDet:AddUser,userCreds:Credentials,request:Request):
        db=request.state.db
        password=HashPassword(userCreds.password)
        user= sec.sign_up(user=user.Id,password=password,db=db)
       
    @auth.post("/login")
    async def login(self, user:Credentials,request:Request):
        db=request.state.db
        h_pwd=
        VerifyPassword()

    @auth.put("/logout")
    async def logout(self):
        pass

    @auth.post("/forgot/password")
    async def verify_username(self,user:ResetCredentials,request:Request):
        db=request.state.db
        password=user.password
        

    @auth.post(path="/reset/password")
    async def change_password(self, user:UpdateCredentials,request:Request):
        db=request.state.db
        
