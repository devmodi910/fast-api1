from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#sqlite 
SQLALCHEMY_DATABSE_URL = 'sqlite:///./todosapp.db'


# postgres
# SQLALCHEMY_DATABSE_URL = 'postgresql://postgres:LANET@localhost/TodoApplicationDatabase'

#mysql
# SQLALCHEMY_DATABSE_URL = 'mysql+pymysql://root:LANET@127.0.0.1:3306/TodoApplicationDatabase'

engine = create_engine(SQLALCHEMY_DATABSE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()