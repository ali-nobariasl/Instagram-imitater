from sqlalchemy.orm.session import Session
from fastapi import HTTPException ,status
from router.schemas import UserBase
from db.models import DbUser
from db.hashing import Hash

def create_new_user(request:UserBase, db:Session):
    user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db:Session,username:str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User not found')
    return user

def get_all_users(db:Session):
    users = db.query(DbUser).all()
    return users