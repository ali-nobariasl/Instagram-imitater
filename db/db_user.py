from sqlalchemy.orm.session import Session

from router.schemas import UserBase
from db.models import DbUser
from db.hashing import Hash

def create_new_user(request:UserBase, db:Session):
    user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user