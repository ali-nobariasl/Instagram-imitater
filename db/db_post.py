from datetime import datetime
from sqlalchemy.orm.session import Session

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