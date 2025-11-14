from pydantic import BaseModel
from typing import Optional

class  PackageBill(BaseModel):
    package: str
    amount : float
    id : Optional[str|int]

# class UpgradePackage(BaseModel):
