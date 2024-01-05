from sqlalchemy.orm.session import Session
from datetime import datetime
from db.models import DbComment
from router.schemas import CommentBase
from fastapi import APIRouter, Depends

from db import db_comment
from db.database import get_db


router = APIRouter(prefix='/comment', tags=['comment'])


@router.get('/all/{post_id}')
def get_comments( post_id:int,db:Session= Depends(get_db)):
    return db_comment.get_all_comments(db, post_id)

