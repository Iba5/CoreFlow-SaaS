from sqlalchemy import create_engine
from app.utils.configs import config

if config.DB_URL:
    engine = create_engine(config.DB_URL,isolation_level="AUTOCOMMIT")



"""
so since we used optional we should 
first check if the url is not none
then we assign the url and create the
engine
"""