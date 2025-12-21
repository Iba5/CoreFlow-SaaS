from typing import Optional,List
from models.MemberTables import Workers
from models.Member import user,Switch,AssignUser,Total_Emp
from abc import ABC,abstractmethod

class CompanyRepo(ABC):
    #Company EMployee
    @abstractmethod
    def Add_New_User(self,detail:user,db:Session):
        pass
    @abstractmethod
    def Update_User_Access(self,id:Optional[int|str],role:AssignUser,db):
        pass
    @abstractmethod
    def Change_User_Details(self,id:Optional[int|str],details:Switch):
        pass
    @abstractmethod
    def Get_User_Detail(self,id:Optional[int|str]):
        pass
    @abstractmethod
    def Get_All_Users(self):
        pass
    @abstractmethod
    def Delete_User(self,id:Optional[int|str]):
        pass
    @abstractmethod
    def Count_Department(self)->List[Total_Emp]:
        pass
    @abstractmethod
    def Count_All(self)->Total_Emp:
        pass
    

class CompanyUser(CompanyRepo):
    pass
