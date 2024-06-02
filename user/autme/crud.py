"""
Регистрация нового пользователя в системе
"""
import datetime
from typing import Tuple, Dict

import jwt
from fastapi import Request

from base.main import *
from config import SECRET_KEY
from user.md5.convert_md5 import calculate_md5
from user.model.model_autme import user_autme
from fastapi.responses import JSONResponse


def autme_user(users: user_autme, request: Request):

    result = session.query(autme).filter(autme.mail == users.mail)
    for i in result:
        if calculate_md5(users.password) != i.password:
            return JSONResponse({"message": "Пароль не верный"}, status_code=401)
        new_device = device()
        new_device.ip_device = request.client.host
        new_device.name_device = users.name_device
        new_device.operation_system = users.os
        new_device.version_program = users.version_program
        session.add(new_device)
        token = jwt.encode({"mail": users.mail, "nickname": i.user_realt.nickname, "role": i.role, "date": str(datetime.datetime.today())}, SECRET_KEY, algorithm="HS256")
        new_autme_user = token_autme()
        new_autme_user.token = token
        new_autme_user.mail = users.mail
        new_autme_user.device = new_device.id
        session.add(new_autme_user)
        session.commit()
        return {"message": "Успешная авторизация", "token": token}
    return JSONResponse({"message": "Такого пользователя не найдено"}, status_code=401)
