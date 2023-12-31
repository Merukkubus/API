from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy

cookie_transport = CookieTransport(cookie_name="languages",cookie_max_age=3600)

SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)