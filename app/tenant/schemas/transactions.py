from enum import Enum
from pydantic import BaseModel,field_serializer, field_validator
from typing import Optional,Any
from datetime import datetime,date

class Status(str,Enum):
    profit="profit"
    loss="loss"

class AddTrans(BaseModel):
    Description:    str
    Amount:         float
    Type:           Status
    user_id:        Optional[int|str]


class DisplayUser(BaseModel):
    Description:    str
    Amount:         float
    Type:           Status
    Date:           datetime
    user_id:        int

    @field_serializer("Date")
    def ToHuman(cls,v:datetime,_info:Any)->str:
        return v.strftime("%d %m %Y")


class RangeOfTrans(BaseModel):
    StartDate:  date
    EndDate:    date

    @field_validator("StartDate","EndDate",mode="before")
    def checking(cls,v:str)->date:
        formats = ["%d/%m/%Y","%d-%m-%Y"]
        for fmt in formats:
            try:
                return datetime.strptime(v,fmt).date()
            except:
                pass
        raise ValueError("Invalid date format: start with Dare->Month->Year and use '/' or '-'")

    @field_validator("EndDate")
    def range(cls, v:date,values:Any):
        start = values.data.get("StartDate")
        if start and v<start:
            raise ValueError("End date cannot be less than start")
        return v

class DisplayTransPeriodic(BaseModel):
    Description:    str
    Amount:         float
    Date:           datetime

    @field_serializer("Date")
    def ToHuman(cls,v:datetime,_info:Any)->str:
        return v.strftime("%d %m %Y")
