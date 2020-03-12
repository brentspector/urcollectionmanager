from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# The declarative_base object to be used by all classes
Base = declarative_base()

# Creates a SQLAlchemy base of operations
engine = create_engine('sqlite:///data/collection.sqlite')

def _create_all():
    Base.metadata.create_all(engine)

def get_session():
    _create_all()
    return sessionmaker(bind=engine)()