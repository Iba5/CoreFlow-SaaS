from pydantic import BaseModel, field_serializer,field_validator
from typing import Optional,Any
from datetime import date,datetime

class signin(BaseModel):
    firstname : str
    middlename: Optional[str]
    lastname:   str
    DOB:        date
    gender:     str
    
    @field_validator("DOB",mode="before")
    def to_date(cls,v:str):
        formats=["%d/%m/%Y","%d-%m-%Y"]
        for format in formats:
            try:
                return datetime.strptime(v,format).date()
            except:
                pass
        raise ValueError("Wrong date format use DD/MM/YYYY or DD-MM-YYYY")
    

class credentials(BaseModel):
    id      :   int
    username:   str
    password:   str

class login(BaseModel):
    username: str
    password: str

class display(BaseModel):
    username:   str
    firstname : str
    middlename: Optional[str]
    lastname:   str
    DOB:        date
    gender:     str

    @field_serializer("DOB")
    def to_human(cls,v:date,_info:Any):
        return v.strftime("%d/%m/%Y")