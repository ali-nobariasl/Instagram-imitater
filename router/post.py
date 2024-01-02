from fastapi import APIRouter, Depends, status
from fastapi.exceptions import  HTTPException
from sqlalchemy.orm.session import Session

from db.models import DbPost
from router.schemas import PostBase, PostDisplay
from db import db_post
from db.database import get_db

router = APIRouter(prefix='post',tags=['post'])

imag_url_types = ['absolute', 'relative']

@router.post('/post', response_model=PostDisplay)
def create_new_post(request:PostBase, db:Session= Depends(get_db)):
    if not request.img_url_type in imag_url_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='imagr url types could accpete absulut and relative values')
    
    
    return db_post.create_post(request, db)