from sqlalchemy import Integer, Column, create_engine, ForeignKey
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None

# Stock info will be passed in as an instance of this class
class Stock_Data(Base):
    # __tablename__ = 
    id = Column()


#Do a database check to see if a table exists for our data yet.
#If there is no table, create an instance of the table for the SQLALCHEMY ORM
class Create_Table:
    def table_info(self,w,x,y,z):
        pass
