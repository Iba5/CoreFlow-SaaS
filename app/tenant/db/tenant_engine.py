from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from utils.configs import config

TenantBase = declarative_base()

def createEng(db_name:str):
    from tenant.models.MemberTables import Workers,Finances # type: ignore
    if config.TENANT_URL:
        engine = create_engine(config.TENANT_URL+db_name)
        TenantBase.metadata.create_all(bind=engine)
        return engine
    

"""
This tenant_engine.py is the one responsible
for dynamically creating tenant dbs
this is created upon new addition of a tenant
"""