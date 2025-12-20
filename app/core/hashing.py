from passlib.context import CryptContext

pwd_hash = CryptContext(
     schemes=["bcrpyt"], #hashing algorithm
    deprecated="auto", #allow future upgrades
    )

def HashPassword(plain:str)->str:
    return pwd_hash.hash(plain)

def VerifyPassword(plain:str,hashed_pwd:str)->bool:
    return pwd_hash.verify(plain,hashed_pwd)
