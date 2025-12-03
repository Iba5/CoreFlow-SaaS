from pydantic import BaseModel
from typing import Optional

class AddUser(BaseModel):
    Firstname:  str
    Middlename: Optional[str]
    Lastname:   str
    DOB:        str
    Gender:     str

class UpdateUser(BaseModel):
    Firstname:  Optional[str]
    Middlename: Optional[str]
    Lastname:   Optional[str]
    DOB:        Optional[str]
    Gender:     Optional[str]
    

class Credentials(BaseModel):
    Id:         Optional[str|int]
    username:   str
    password:   str

class UpdateCredentials(BaseModel):
    Id:     Optional[str|int]
    oldpwd: str
    newpwd: str

class ResetCredentials(BaseModel):
    Id:     Optional[str|int]
    newpwd: str
