import ormar

from fastapi_users.db import OrmarBaseUserModel, OrmarUserDatabase

from db import MainMeta
from user.schemas import UserDB


class User(OrmarBaseUserModel):
    class Meta(MainMeta):
        pass

    username: str = ormar.String(max_length=100, unique=True)
    phone: str = ormar.String(max_length=14, unique=True)


user_db = OrmarUserDatabase(UserDB, User)
