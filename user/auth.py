from fastapi_users.authentication import JWTAuthentication
from user.schemas import User, UserDB, UserCreate, UserUpdate
from fastapi_users import FastAPIUsers


from user.models import user_db

SECRET = "Ssldfk$9dksl98943kd_Kdf(*@#kkd983lksdpa83r32kLKJE9o8ej:WJ{F"

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)


fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB
)

current_active_user = fastapi_users.current_user(active=True)
