"""
Регистрация нового пользователя в системе
"""
import datetime
from typing import Tuple, Dict

from base.main import *
from user.md5.convert_md5 import calculate_md5
from user.model.user import new_user
from fastapi.responses import JSONResponse


def create_user(users: new_user):

    result = session.query(autme).filter(autme.mail == users.mail)
    for i in result:
        return JSONResponse({"message": "Такая почта уже зарегистрированная"}, status_code=400)
    result = session.query(user).filter(user.nickname == users.nickname)
    for i in result:
        return JSONResponse({"message": "Такое имя пользователя уже занято"}, status_code=400)
    n_autme = autme(role=1, mail=users.mail, password=calculate_md5(users.password))
    session.add(n_autme)
    age = datetime.datetime(int(users.age.split(".")[2]), int(users.age.split(".")[1]), int(users.age.split(".")[0]))
    n_user = user(subscription=1, FIO=users.fio, phone=users.phone, nickname=users.nickname, mail=users.mail, birthday=age)
    session.add(n_user)
    session.commit()

    return {'success': 'Пользователь успешно зарегестрирован'}
