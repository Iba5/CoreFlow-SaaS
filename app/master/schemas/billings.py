from pydantic import BaseModel

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
    Date:       str
    Expiry:     str
    Remain:     int
    