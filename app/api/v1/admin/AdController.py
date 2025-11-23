from fastapi import APIRouter
from starlette.requests import Request

class AdminController:
    adm = APIRouter(prefix="/admin",tags=["Admin"])

    # assume hr is the admin
    @adm.post("/addWorker")
    async def addWorker(self,request:Request):
        pass
    @adm.put("/team")
    async def ReAllWorker(self,request:Request):
        pass
    @adm.delete("/remove/{id}")
    async def DeleteUser(self,request:Request):
        pass

    #manager
    @adm.post("/tasks/new")
    async def AddTask(self,request:Request):
        pass

    #finance
    @adm.get(path="/transactions")
    async def summary(self,request:Request):
        pass
    @adm.get(path="/payroll")
    async def pays(self, request:Request):
        pass