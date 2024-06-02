from datetime import datetime
from fastapi import APIRouter
from pydantic import EmailStr
from fastapi import Request

from user import crud
from user.check_code import crud as crud_user_code
from user.model.model_autme import user_autme
from user.model.model_get_code import get_user_code
from user.model.user import new_user
from user.model.model_user_code import m_user_code
from user.send_code import send_code
from user.autme import crud as autme_user


autohorizen = APIRouter()

print(f"[{datetime.today().strftime('%H:%M:%S')}] [API] Registration initialization was completed successfully")


@autohorizen.post("/register")
def register(user: new_user):
    return crud.create_user(user)


@autohorizen.post("/code")
def check_user_code(us_code: m_user_code):
    return crud_user_code.check_user(us_code)


@autohorizen.get("/code")
def check_user_code(email: EmailStr):
    return send_code.send_user_code(email)


@autohorizen.post("/autme")
def check_user_code(users: user_autme, request: Request):
    return autme_user.autme_user(users, request)
