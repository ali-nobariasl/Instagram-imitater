from fastapi import APIRouter, Depends, status ,UploadFile, File
from fastapi.exceptions import  HTTPException
from sqlalchemy.orm.session import Session
import random, string, shutil
from db.models import DbPost
from router.schemas import PostBase, PostDisplay
from db import db_post
from db.database import get_db
from router.schemas import UserAuth
from auth.oauth2 import get_current_user


router = APIRouter(prefix='/post',tags=['post'])

imag_url_types = ['absolute', 'relative']

@router.post('/post', response_model=PostDisplay)
def create_new_post(request:PostBase, db:Session= Depends(get_db),current_user:UserAuth= Depends(get_current_user)):
    if not request.img_url_type in imag_url_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail='imagr url types could accpete absulut and relative values')
    return db_post.create_post(request, db)


@router.get('/get_all',response_model=PostDisplay)
def get_all_posts(db:Session= Depends(get_db)):
    return db_post.get_posts(db)


@router.post('/uploudimage')
def upload_image(image:UploadFile=File(...), current_user:UserAuth= Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.',1))
    path = f'images/{filename}'
    
    with open(path,"w+b") as f:
        shutil.copyfileobj(image.file, f)
        
    return {'filename': path}


@router.get('/delete/{id}')
def delete_post(id:int, db:Session= Depends(get_db), current_user: UserAuth=Depends(get_current_user) ):
    return db_post.delete(id, db, current_user.id)