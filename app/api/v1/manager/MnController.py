from fastapi import APIRouter
from starlette.requests import Request

class ManagerController:
    manage = APIRouter(prefix="/manager",tags=["manager"])

    @manage.post("/tasks/new")
    async def AddTask(self,request:Request):
        pass

    @manage.put("/tasks/{id}")
    async def Completed(self,request:Request):
        pass

    @manage.get("/tasks/all")
    async def GetAllTasks(self):
        pass

    @manage.get(path="/{id}/team")
    async def get_team(self,request:Request):
        pass