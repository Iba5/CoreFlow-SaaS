from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.responses import Response
from sqlalchemy.orm import sessionmaker
from typing import Callable,Awaitable
from app.master.repos.MasterRepo import get_dbname
from app.tenant.db.tenant_engine import get_tenant_db


class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request : Request,call_next: Callable[[Request],Awaitable[Response]])->Response:
        # extract dbname from the request header
        Company_id=int(request.headers["Company_Id"])
        #checks if it is none or what
        if not Company_id:
            return JSONResponse("Invalid Id" ,status_code=400)
        # access dbname from the master repo
        db_url= await get_dbname(Company_id)
        if not db_url:
            return JSONResponse("Invalid Credentials", status_code=400)
        engine = await get_tenant_db(db_url)
        # a session is created based on the user or request
        SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
        db=SessionLocal()
        # the db session is passed into the request
        request.state.db= db
        try:
            response =await call_next(request)
        finally:
            db.close()
        
        return response
    
