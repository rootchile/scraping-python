from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///newspaper.db')

Session = sessionmaker(bind=engine)

# clase base para extender modelos
Base = declarative_base()