from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date,datetime

class AddUser(BaseModel):
    Firstname:  str
    Middlename: Optional[str]
    Lastname:   str
    DOB:        date
    Gender:     str

    @field_validator("DOB",mode="before")
    def to_date(cls,v:str):
        formats = ["%d/%m/%Y","%d-%m-%Y"]
        for fmt in formats:
            try:
                return datetime.strptime(v,fmt).date()
            except:
                pass
        raise ValueError("Invalid DateFormat: DD/MM/YYYY or DD-MM-YYYY")

class UpdateUser(BaseModel):
    Firstname:  Optional[str]
    Middlename: Optional[str]
    Lastname:   Optional[str]
    DOB:        Optional[date]
    Gender:     Optional[str]
    
    @field_validator("DOB",mode="before")
    def to_date(cls,v:str):
        if not v :
            return None
        
        formats = ["%d/%m/%Y","%d-%m-%Y"]
        for fmt in formats:
            try:
               return datetime.strptime(v,fmt).date()
            except:
                pass
        raise ValueError("Invalid DateFormat: DD/MM/YYYY or DD-MM-YYYY")

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
