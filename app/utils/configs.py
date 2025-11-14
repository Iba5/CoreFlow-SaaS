from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URL:     Optional[str] = None
    SECRET:     Optional[str] = None
    ALGO:       Optional[str] = None
    TENANT_URL: Optional[str] =None
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
config = Settings()

# print(config.DB_URL)
"""
Lesson for today and the config file
to avoid pydantic errors we are supposed 
to make use of Optional
this is because we are importing secret
keys, hence we are not parsing
them but expecting to retrieve them
and this violates pydantic

the optional then gives a default none however
there will be a value when we try to access it
"""