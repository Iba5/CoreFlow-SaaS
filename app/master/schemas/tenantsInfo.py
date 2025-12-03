from pydantic import BaseModel
from typing import Optional

class signin(BaseModel):
    firstname : str
    middlename: Optional[str]
    lastname:   str
    DOB:        str
    gender:     str

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
    DOB:        str
    gender:     str
