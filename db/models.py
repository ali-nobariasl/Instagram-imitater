from sqlalchemy import Column, Integer, String, DateTime

from .database import Base


class DbUser(Base):
    #__tabelename__ = 'user'
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    
    
class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    caption: Column(String)
    img_url : Column(String)
    img_url_type : Column(String)
    timestamp : Column(DateTime)