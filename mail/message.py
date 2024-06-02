from random import randint
from threading import Thread

from mail.send.send import send
from mail.config import *


class send_mail:


    def send_code_register(self, send_adress, code):
        message = f"Добро пожаловать в программу EcoMusic! Ваш код регистрации"
        subject = "Код подтверждения регистрации"
        Thread(target=send, args=(send_adress, code, smtp_password, from_email, smtp_server, smtp_port, message, subject, )).start()


    def send_code(self, send_adress, operation=None):
        code = randint(100000, 999999)
        message = f"Вы начали {operation} в программе EcoPoint. Введите код."
        subject = "Код подтверждения операции"
        Thread(target=send, args=(send_adress, code, smtp_password, from_email, smtp_server, smtp_port, message, subject, )).start()
        return code


    def send_message(self, send_adress, message):
        code = randint(100000, 999999)
        subject = "Код подтверждения операции"
        Thread(target=send, args=(send_adress, code, smtp_password, from_email, smtp_server, smtp_port, message, subject, )).start()
        return code
