from fastapi import APIRouter
from starlette.requests import Request

class AccController:
    acc=APIRouter(prefix="/accountant",tags=["Finance"])

    @acc.put("/salary/{department}/{id}")
    async def update_salary(self,request:Request):
        pass

    @acc.post(path="/transactions/add")
    async def add_trans(self):
        pass
    
    @acc.get(path="/transactions/{id}")
    async def get_trans(self,request:Request):
        pass
    
    @acc.get(path="/transactions/all")
    async def get_all(self):
        pass
    
    @acc.get(path="/transactions/{id}")
    async def get_by_id(self,request:Request):
        pass

    @acc.get(path="/payroll")
    async def get_payroll(self):
        pass

    @acc.get(path="/payroll/{department}")
    async def get_dept_payroll(self, request:Request):
        pass

    acc.get("/transactions/total")
    async def total_costs(self):
        pass

