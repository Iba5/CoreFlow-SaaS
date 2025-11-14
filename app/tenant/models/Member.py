from pydantic import BaseModel
from typing import Optional

#this is how the user will add his data before role is initialised
class user(BaseModel):
    username :      str
    password :      str
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

    """
    so here where it gets interesting
    each class has its own purpose based 
    on functionalities
    """