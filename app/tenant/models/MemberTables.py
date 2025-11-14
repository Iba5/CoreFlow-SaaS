from tenant.db.tenant_engine import TenantBase
from sqlalchemy import Column,Integer,String,Numeric,DateTime,ForeignKey
from datetime import datetime

class Workers(TenantBase):
    __tablename__="workers"
    id          =Column(Integer,primary_key=True)
    username    =Column(String,nullable=False)
    password    =Column(String,nullable=False)
    firstname   =Column(String,nullable=False)
    middlename  =Column(String,nullable=True)
    lastname    =Column(String,nullable=False)
    age         =Column(Integer,nullable=False)
    gender      =Column(String,nullable=False)
    dow         =Column(DateTime,default=datetime.now(),nullable=False)
    salary      =Column(Numeric(5,2),nullable=True)
    role        =Column(String,nullable=True)
    leader      =Column(Integer,nullable=True)


class Finances(TenantBase):
    __tablename__="finances"
    trans_id    =Column(Integer,primary_key=True)
    finances    =Column(String,nullable=False,index=True)
    amount      =Column(Numeric(10,2),nullable=False)
    date        =Column(DateTime,default=datetime.now(),nullable=False)
    user_id     =Column(Integer,ForeignKey("workers.id"))

"""
so here I have created 2 tables
1. contains the details of the workers 
    which will be falling under a certain leader
    if it exists
2. Finances table which is responsible for
    keeping track of the money used or recieved
    by the company
"""