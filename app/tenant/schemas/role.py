from typing import Optional
from pydantic import BaseModel

class RoleCreation(BaseModel):
    Role:   str

class EndPoints(BaseModel):
    route:  str

class AssignRole(BaseModel):
    role:   Optional[str|int]
    user:   Optional[str|int]

class RoleEndpoint(BaseModel):
    RoleId:   Optional[str|int]
    EndpointId:  Optional[str|int]