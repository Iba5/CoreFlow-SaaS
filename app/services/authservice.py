from sqlalchemy.orm import Session 
from app.tenant.schemas.userAdd import AddUser

class AuthService:
    def log_in(self,user:str|int,db:Session):
        pass
    def sign_up(self,user:AddUser,username:str,password:str,db:Session):
        pass
    def log_out(self,db:Session):
        pass
    def reset_password(self,user:int|str,password:str,db:Session):
        pass
    def update_password(self,user:int|str,pwd:str):
        pass