from fastapi import APIRouter, Depends
from fastapi.param_functions import AOuth2PasswordRequestForm 
from sqlalchemy.orm.session import Session

from db.database import get_db
from db.models import DbUser


router = APIRouter(tags=['authentication'])

@router.post('/login')
def login(request:AOuth2PasswordRequestForm= Depends(), db:Session=Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username == request.user.username).first()
    if not user:
        