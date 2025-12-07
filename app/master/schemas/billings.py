from pydantic import BaseModel,field_serializer
from datetime import date
from typing import Any

class bill(BaseModel):
    PackId:  str
    TenantId:   str

class subscription(BaseModel):
    Package:    str
    Duration:   int
    Cost:       float

class displayBill(BaseModel):
    Package:    str
    Duration:   int
    Cost:       float
    Date:       date
    Expiry:     date
    Remain:     int

    @field_serializer("Date","Expiry")
    def to_human(cls,v:date,_info:Any):
        return v.strftime("%d/%m/%Y")

    