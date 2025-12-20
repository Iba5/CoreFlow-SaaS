from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URL:     str
    SECRET:     str
    ALGO:       str
    TENANT_URL: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
config = Settings() # type: ignore

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