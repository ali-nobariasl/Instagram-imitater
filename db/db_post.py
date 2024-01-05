import datetime
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from db.models import DbPost
from router.schemas import PostBase


def create_post(request:PostBase, db:Session):
    new_post = DbPost(
        caption= request.caption , 
        img_url = request.img_url,
        img_url_type=request.img_url_type,
        timestamp = datetime.datetime.now(),
        user_id = request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts(db:Session):
    posts = db.query(DbPost).all()
    
    return posts
    
    
def delete(id:int, db:Session,user_id:int ):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='the post was not found')
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only post creator can delete the post')
    
    db.delete(post)
    db.commit()
    return "Ok Baby :)"