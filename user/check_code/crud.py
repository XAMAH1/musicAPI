"""
Регистрация нового пользователя в системе
"""
import datetime
from typing import Tuple, Dict

from base.main import *
from user.model.model_user_code import m_user_code
from fastapi.responses import JSONResponse


def check_user(users: m_user_code):

    result = session.query(autme).filter(autme.mail == users.mail, autme.isActive == True)
    for i in result:
        return JSONResponse({"message": "Почта уже прошла валидацию"}, status_code=400)

    success_code = False
    result = session.query(user_code).filter(user_code.mail == users.mail)
    for i in result:
        if i.mail != users.mail:
            return JSONResponse({'message': "Код не верный!"}, status_code=400)
        if i.isUse:
            return JSONResponse({"message": 'Код уже активирован'}, status_code=400)
        if i.code != users.user_code:
            return JSONResponse({'message': "Код не верный!"}, status_code=400)
        day_code = str(i.date_create).split(" ")
        date = datetime.datetime(int(day_code[0].split("-")[0]),
                                 int(day_code[0].split("-")[1]),
                                 int(day_code[0].split("-")[2]),
                                 int(day_code[1].split(":")[0]),
                                 int(day_code[1].split(":")[1]),
                                 int(day_code[1].split(":")[2])
                                 )
        if date + datetime.timedelta(hours=int(str(i.time).split(":")[0]), minutes=int(str(i.time).split(":")[1])) < datetime.datetime.today():
            return JSONResponse({"message": "Код больше не действителен"}, status_code=400)
        success_code = True
        i.user_realt.autme_realt.isActive = True
    if not success_code:
        return JSONResponse({"message": "Код не найден"}, status_code=400)
    session.query(user_code).filter(user_code.mail == users.mail).delete()
    session.commit()

    return {'success': 'Код успешно активирован'}
