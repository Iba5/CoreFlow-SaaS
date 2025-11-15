from sqlalchemy.orm import sessionmaker
from db.engine import engine

session = sessionmaker(bind=engine,autocommit=False,autoflush=False)