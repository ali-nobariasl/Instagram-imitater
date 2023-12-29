from sqlalchemy.orm.session import Session

from router.schemas import UserBase
from db.models import DbUser


def create_new_user(request:UserBase, db:Session):
    user = DbUser(
        username = request.username,
        email = request.email,
        password = request.password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user