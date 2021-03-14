from datetime import datetime
from typing import Optional, Union, Dict
from db import MainMeta

import ormar
from user.models import User


class Video(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=50)
    description: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=1000)
    create_at: datetime = ormar.DateTime(default=datetime.now)
    user: Optional[Union[User, Dict]] = ormar.ForeignKey(User)
