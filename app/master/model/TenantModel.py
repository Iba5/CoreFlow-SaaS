from typing import Optional
from pydantic import BaseModel

class AddTenant(BaseModel):
    firstname :     str
    middlename :    Optional[str] = None
    lastname :      str
    gender :        str
    username :      str
    password :      str
    db_name :       str
    active :        bool

class UpdateTenant(BaseModel):
    active: bool

class DisplayTenant(BaseModel):
    firstname :     str
    middlename :    Optional[str] = None
    lastname :      str
    gender :        str
    username :      str
    db_name :       str
    active :        bool


