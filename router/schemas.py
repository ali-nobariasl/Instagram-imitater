from pydantic import BaseModel
from datetime import datetime
from typing import List

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
    creator_id : int

# for postdisplay
class User(BaseModel):
    username : str
    class Confing():
        orm_mode = True

# for postdisplay
class Comment(BaseModel):
    text: str
    username: str
    timestampe: datetime
    class Confing():
        orm_mode = True
    

class PostDisplay(BaseModel):
    id : int
    caption: str
    img_url : str
    img_url_type : str
    timestamp : datetime
    user: User
    comment : List[Comment]
    class Confing():
        orm_mode = True
        
class CommentBase(BaseModel):
    post_id: int
    username : str
    text : str
       
class CommentDisplay(BaseModel):
    id : int
    content: str
    user_id : int
    post_id : int
    timestamp : datetime
    user: User
    class Confing():
        orm_mode = True
        
        
class UserAuth(BaseModel):
    id : int
    usernmae: str
    email: str