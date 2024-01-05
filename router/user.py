from sqlalchemy.orm.session import Session
from fastapi import Depends, APIRouter
from router.schemas import UserBase
from db.models import DbUser
from db.db_user import create_new_user,get_all_users
from db.database import get_db


router = APIRouter(prefix='/user', tags=['user'])


@router.post('/')
def create_user(request:UserBase, db:Session=Depends(get_db)):
    return create_new_user(request, db)

@router.get('/getuser')
def get_user(db:Session=Depends(get_db)):
    return get_all_users(db)