from sqlalchemy import Column,Integer,String,Numeric,DateTime,Boolean,ForeignKey
from db.base import BaseMaster
from datetime import datetime

class Tenants(BaseMaster):
    __tablename__="tenants"

    id =            Column(Integer,primary_key=True,index=True)
    first_name =    Column(String,nullable=False)
    middle_name=    Column(String,nullable=True)
    last_name=      Column(String,nullable=False)
    gender=         Column(Integer,nullable=False)
    username=       Column(String,nullable=False)
    password=       Column(String,nullable=False)
    db_name=        Column(String, nullable=False)
    active=         Column(Boolean,default=True)


class Billings(BaseMaster):
    __tablename__="billing"
    trans_id =  Column(Integer,primary_key=True)
    package =   Column(String,nullable=False)
    amount =    Column(Numeric(10,2),nullable=False)
    dot =       Column(DateTime,default=datetime.now())
    tenat_id=   Column(Integer,ForeignKey("tenants.id"))



"""
This is the MasterDb Setup
it comprises of the 
1. Tenants Details
2. Billings History
3. Packages


the relationship of tenants to billings 
is 1 tenant to many billings
"""