from pydantic import BaseModel
from typing import Optional

#this is how the user will add his data before role is initialised
class user(BaseModel):
    username :      str
    password :      str
    company:        str
    firstname :     str
    middlename :    Optional[str] = None
    lastname :      str
    age:            int
    gender :        str

#Here either managers of the finance can actually manipulate data such as raising salary change role or both
class Switch(BaseModel):
    role:   Optional[str]
    salary: Optional[float]

#here after creation role is assigned by others
class AssignUser(BaseModel):
    salary:         float
    role:           str
    leader:         Optional[int]=None

class Display_User(BaseModel):
    username:       str
    company:        str
    firstname :     str
    middlename :    Optional[str] = None
    lastname :      str
    age:            int
    gender :        str

class Display_Work_Details(BaseModel):
    username:   str
    salary:     float
    role:       str
    leader:     Optional[int]=None

class Total_Emp(BaseModel):
    total:  int
    role:   Optional[str]

class Finance(BaseModel):
    finance:    str
    amount:     float
    date:       str

class Finance_By_User(BaseModel):
    username:   str
    finance:    str
    amount:     float
    date:       str

class Add_Trans(BaseModel):
    finance:    str
    amount:     float
    expense:    bool
    user_id:    Optional[int|str]

class Totals(BaseModel):
    expnse : Optional[float]
    profit : Optional[float]
    All :    Optional[float]

    """
    so here where it gets interesting
    each class has its own purpose based 
    on functionalities
    """