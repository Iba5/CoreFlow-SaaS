from typing import Optional,List
from models.MemberTables import Workers,Finances
from models.Member import Finance,Finance_By_User,Totals,Add_Trans
from abc import ABC,abstractmethod

class FinanceRepo(ABC):
    #Financial Side
    @abstractmethod
    def Display_User_Trans(self,id:Optional[int|str])->List[Optional[Finance_By_User]]:
        pass
    @abstractmethod
    def Add_trans(self,details:Add_Trans)->Finance:
        pass
    @abstractmethod
    def Display_Recent_Trans(self):
        pass
    @abstractmethod
    def Display_All_Trans(self)->List[Finance]:
        pass
    @abstractmethod
    def Total_Funds(self)->Totals:
        pass
    @abstractmethod
    def Total_Income(self)->Totals:
        pass
    @abstractmethod
    def Total_Expense(self)->Totals:
        pass

class CompanyFinance(FinanceRepo):
    pass