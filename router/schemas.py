from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username : str
    email   : str
    password    : str
    
class UserDisplay(BaseModel):
    username : str
    email   : str
    class Config():
        orm_mode= True
        

     
class PostBase(BaseModel):
    caption: str
    img_url : str
    img_url_type : str
    creator_id : str

class User(BaseModel):
    username : str
    class Confing():
        orm_mode = True

class PostDisplay(BaseModel):
    id : int
    caption: str
    img_url : str
    img_url_type : str
    timestamp : datetime
    user: User
    class Confing():
        orm_mode = True
        
        
class CommentDisplay(BaseModel):
    id : int
    content: str
    user_id : int
    post_id : int
    timestamp : datetime
    user: User
    class Confing():
        orm_mode = True