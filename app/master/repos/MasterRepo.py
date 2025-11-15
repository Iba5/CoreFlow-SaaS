from typing import List, Optional
from sqlalchemy import or_,text
from abc import ABC, abstractmethod
from master.model.TenantModel import AddTenant,UpdateTenant,DisplayTenant
from master.model.BillingModel import PackageBill,DisplayHistory
from master.model.table import Tenants,Billings
from master.db.session import session

db=session()

class MasterRepo(ABC):
    @abstractmethod
    def Add_Tenant(self,data:AddTenant)->DisplayTenant:
        pass
    @abstractmethod
    def Update_Tenant(self,id:Optional[int|str],data:UpdateTenant):
        pass
    @abstractmethod
    def Delete_Tenant(self, id:Optional[int|str]):
        pass
    @abstractmethod
    def Get_Tenant(self,data:Optional[int|str])->DisplayTenant:
        pass
    @abstractmethod
    def Get_All_Tenant(self)-> List[DisplayTenant]:
        pass
    @abstractmethod
    def Get_Tenant_Bills(self, id:Optional[int|str])->List[Optional[DisplayHistory]]:
        pass
    @abstractmethod
    
    @abstractmethod
    def Display_all_funds(self)->List[DisplayHistory]:
        pass
    @abstractmethod
    def Update_Package(self, details:PackageBill)-> Optional[DisplayHistory]:
        pass

class Tenant_Data(MasterRepo):
    def __init__(self):
        self.db=db
    
    def Add_Tenant(self, data: AddTenant)->DisplayTenant:
        new_user=Tenants(**data.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.execute(text(f"CREATE DATABASE {new_user.db_name}"))
        self.db.commit()
        self.db.refresh(new_user)
        return DisplayTenant.model_validate(new_user)
    
    def Update_Tenant(self, id:Optional[int|str],data: UpdateTenant):
        details = data.model_dump()
        tenant = self.db.query(Tenants).filter(or_(Tenants.id==id,Tenants.username==id)).first()
        for key, value in details.items():
            setattr(tenant,key,value)
        self.db.commit()
        self.db.refresh(tenant)
    
    def Delete_Tenant(self, id:Optional[int|str]):
        tenant = self.db.query(Tenants).filter(or_(Tenants.id==id,Tenants.username==id)).first()
        if tenant is not None:
            self.db.execute(text(f"DROP DATABASE {tenant.db_name}"))
            self.db.delete(tenant)
            self.db.commit()
            return tenant
        return None
        

    def Get_Tenant(self,data:Optional[int|str])->DisplayTenant:
        tenant =self.db.query(Tenants).filter(or_(Tenants.id==data,Tenants.username==data)).first()
        return DisplayTenant.model_validate(tenant)

    def Get_All_Tenant(self)->List[DisplayTenant]:
        users = self.db.query(Tenants).all()
        return [DisplayTenant.model_validate(user) for user in users]

class Tenant_Packages(MasterRepo):
    def __init__(self):
        self.db=db
    
    def Get_Tenant_Bills(self, id:Optional[int|str])->List[Optional[DisplayHistory]]:
        if id is None:
            return []
        user=self.db.query(Tenants).filter(or_(Tenants.username==id,Tenants.id==id)).first()
        if user is None:
            return []
        hist = self.db.query(Billings).filter(Billings.tenat_id==user.id).all()
        return [DisplayHistory.model_validate(h) for h in hist]
    
    def Display_all_funds(self)->List[DisplayHistory]:
        funds = self.db.query(Billings).order_by(Billings.trans_id).all()
        return [DisplayHistory.model_validate(f) for f in funds]
    
    
    def Update_Package(self, details:PackageBill)-> Optional[DisplayHistory]: 
        if details.t_id is None:
            return None
        user=self.db.query(Tenants).filter(or_(Tenants.username==details.t_id,Tenants.id==details.t_id)).first()
        if user is None:
            return None
        order = details.model_dump()
        order['t_id']=user.id
        bill = Billings(**order)
        self.db.add(bill)
        self.db.commit()
        self.db.refresh(bill)
        return DisplayHistory.model_validate(bill)
