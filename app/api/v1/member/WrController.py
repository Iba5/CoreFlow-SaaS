from fastapi import APIRouter
from starlette.requests import Request

class WorkersController:
    work= APIRouter(prefix="/worker",tags=["Workers"])
    
    @work.post("/details/{id}")
    async def AddInfo(self, request:Request):
        pass
    @work.put("/update/details/{id}")
    async def UpdateInfo(self, request:Request):
        pass

    @work.get("{id}/task")
    async def GetTask(self,request:Request):
        pass

    @work.get("{id}/info")
    async def GetDetails(self,request:Request):
        pass

    @work.get("{id}/salary")
    async def GetSalaryHistory(self, request:Request):
        pass
