from fastapi import APIRouter
from starlette.requests import Request

class AuthController:
    auth = APIRouter(prefix="/auth",tags=["Authentication"])

    @auth.post("/signin")
    async def SignIn(self,request:Request):
        pass

    @auth.post("/login")
    async def login(self, request:Request):
        pass
    
    @auth.put("/logout")
    async def logout(self):
        pass

    @auth.post("/forgot/password")
    async def verify_username(self,request:Request):
        pass
    @auth.post(path="/reset/password")
    async def change_password(self, request:Request):
        pass
