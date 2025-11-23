from sqlalchemy.orm import declarative_base
from sqlalchemy import Engine, create_engine
from utils.configs import config

TenantBase = declarative_base()
db_url = config.TENANT_URL
engine_cache: dict[str,Engine]={}

def createEng(db_name:str)->Engine:
    if db_name not in engine_cache:
        from tenant.models.MemberTables import Workers,Finances # type: ignore
        engine = create_engine(f"{db_url}{db_name}")
        TenantBase.metadata.create_all(bind=engine)
        engine_cache[db_name]=engine
    return engine_cache[db_name]

async def get_tenant_db(db_name:str):
    return engine_cache[db_name]
    

"""
This tenant_engine.py is the one responsible
for dynamically creating tenant dbs
this is created upon new addition of a tenant
"""