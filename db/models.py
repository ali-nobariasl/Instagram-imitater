from sqlalchemy import Column, Integer, String

from .database import Base


class DbUser(Base):
    #__tabelename__ = 'user'
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)