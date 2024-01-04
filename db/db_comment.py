from sqlalchemy.orm.session import Session
from datetime import datetime
from db.models import DbComment
from router.schemas import CommentBase



def create_comments(db:Session, request:CommentBase):
    new_comment = DbComment(
        context = request.text,
        username = request.username,
        post_id = request.id,
        timestamp =  datetime.now()
    )    
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all_comments(db:Session, post_id:int):
    comments = db.query(DbComment).filter(DbComment.id == post_id)
    return comments