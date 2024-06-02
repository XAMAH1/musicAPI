import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from mail.send import send_html
from mail.send.send_html import get_code


def send(send_adress, code, smtp_password, from_email, smtp_server, smtp_port, message, subject):
    # Создание объекта MIMEMultipart для создания письма
    to_email = send_adress
    msg = MIMEMultipart()
    msg["From"] = f"EcoPoint <{from_email}>"
    msg["To"] = to_email
    msg["Subject"] = subject

    # Добавление текстового содержимого письма
 #   msg.attach(MIMEText(message, "plain"))
    html_body = send_html.get_code(message, code)

    message = message
    msg.attach(MIMEText(html_body, "html"))

    # Создание объекта SMTP и отправка письма
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        try:
            server.login(from_email, smtp_password)
            server.send_message(msg)
        except Exception as e:
            pass
    return
