from sqlalchemy.orm.session import Session
from datetime import datetime
from db.models import DbComment
from router.schemas import CommentBase



def create_comments(db:Session, request:CommentBase):
    new_comment = DbComment(
        text = request.text,
        username = request.username,
        post_id = request.post_id,
        timestamp =  datetime.now()
    )    
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all_comments(db:Session, post_id:int):
    if not post_id:
        print(f"there is no post with {post_id}")
        
    comments = db.query(DbComment).filter(DbComment.post_id == post_id).all()
    return comments



