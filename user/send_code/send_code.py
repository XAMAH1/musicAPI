"""
Отправка кода подтверждения регистрации
"""
import datetime
import random
from typing import Tuple, Dict

from pydantic import EmailStr

from base.main import *
from user.model.model_get_code import get_user_code
from mail.message import send_mail
from fastapi.responses import JSONResponse


def send_user_code(users: EmailStr):

    result = session.query(autme).filter(autme.mail == users)
    if result.count() == 0:
        return JSONResponse({"message": "Вы еще не начинали регистрацию"}, status_code=400)

    session.query(user_code).filter(user_code.mail == users).delete()
    new_code = user_code()
    code = str(random.randint(100000, 999999))
    new_code.code = code
    new_code.mail = users
    new_code.time = "0:10"
    new_code.action = "Регистрация"
    session.add(new_code)
    session.commit()
    send_mail.send_code_register(__name__, users, code)
    return {'message': f'Код отправлен! Проверьте почту {users}'}
