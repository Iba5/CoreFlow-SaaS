from fastapi import APIRouter
from starlette.requests import Request
from tenant.schemas.userAdd import Credentials,ResetCredentials,UpdateCredentials

class AuthController:
    auth = APIRouter(prefix="/auth",tags=["Authentication"])

    @auth.post("/signin")
    async def SignIn(self,user:Credentials,request:Request):
        db=request.state.db
        pass

    @auth.post("/login")
    async def login(self, user:Credentials,request:Request):
        db=request.state.db
        pass

    @auth.put("/logout")
    async def logout(self):
        pass

    @auth.post("/forgot/password")
    async def verify_username(self,user:ResetCredentials,request:Request):
        db=request.state.db

    @auth.post(path="/reset/password")
    async def change_password(self, user:UpdateCredentials,request:Request):
        user 
        db=request.state.db
        pass
