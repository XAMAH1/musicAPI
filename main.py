import datetime

from fastapi import FastAPI
import uvicorn
from user.view import autohorizen
from base.main import *

app = FastAPI()
app.include_router(autohorizen, tags=["Пользователь"])

res = session.query(user_code).filter(user_code.id == 1)
for i in res:
    print(i.date_create)
    print(i.time)
    day_code = str(i.date_create).split(" ")
    date = datetime.datetime(int(day_code[0].split("-")[0]), int(day_code[0].split("-")[1]), int(day_code[0].split("-")[2]),
                             int(day_code[1].split(":")[0]), int(day_code[1].split(":")[1]), int(day_code[1].split(":")[2]))
    if date + datetime.timedelta(hours=int(str(i.time).split(":")[0]), minutes=int(str(i.time).split(":")[1])) < datetime.datetime.today():
        print("Код больше не действителен")
    print(date)

print(f"[{datetime.datetime.today().strftime('%H:%M:%S')}] [API] initialization was completed successfully")

if __name__ == "__main__":
    print(f"[{datetime.datetime.today().strftime('%H:%M:%S')}] [API] initialization has started")
    uvicorn.run("main:app", host='192.168.3.8', port=8000)
