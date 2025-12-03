from enum import Enum
from pydantic import BaseModel
from typing import Optional

class Status(str,Enum):
    profit="profit"
    loss="loss"

class AddTrans(BaseModel):
    Description:    str
    Amount:         float
    Type:           Status
    Date:           str
    user_id:        Optional[int|str]


class DisplayUser(BaseModel):
    Description:    str
    Amount:         float
    Type:           Status
    Date:           str
    user_id:        int

class RangeOfTrans(BaseModel):
    StartDate:  str
    EndDate:    str

class DisplayTransPeriodic(BaseModel):
    Description:    str
    Amount:         float
    Date:           str

