from fastapi import APIRouter
from user.api import after_verification, send_sms_code, after_verification_request

from user.auth import auth_backends, jwt_authentication, SECRET
from user.auth import fastapi_users

user_router = APIRouter()


user_router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
user_router.include_router(
    fastapi_users.get_register_router(send_sms_code), prefix="/auth", tags=["auth"]
)
user_router.include_router(
    fastapi_users.get_verify_router(
        SECRET,
        after_verification_request=after_verification_request,
        after_verification=after_verification
    ),
    prefix="/auth",
    tags=["auth"],
)


user_router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])
