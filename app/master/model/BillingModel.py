from pydantic import BaseModel
from typing import Optional

class  PackageBill(BaseModel):
    package: str
    amount : float
    t_id : Optional[int|str]

class DisplayHistory(BaseModel):
    trans_id: int
    package: str
    amount : float
    t_id : int
    
# class UpgradePackage(BaseModel):
