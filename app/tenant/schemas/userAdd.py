from pydantic import BaseModel, field_serializer, field_validator
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
    Id:         str|int
    username:   str
    password:   str

class UpdateCredentials(BaseModel):
    Id:     str|int
    oldpwd: str
    newpwd: str

class ResetCredentials(BaseModel):
    Id:     str|int
    newpwd: str

class UserResponse(BaseModel):
    id: int
    username: str
    firstname: str
    middlename: str | None
    lastname: str
    gender: str | None
    dob: date

    @field_serializer("dob")
    def human_dob(self, v: date):
        return v.strftime("%d/%m/%Y")
