import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

# SMTP server parameters / Параметры SMTP-сервера
load_dotenv()
smtp_server = os.getenv('SMTP_SERVER')
smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')
smtp_port = 587  # SMTP server port / Порт SMTP-сервера

# Email parameters / Параметры письма
sender = os.getenv('SENDER')  # Sender's address / Адрес отправителя

with open('emails.txt', 'r') as f:  # File with email addresses / Файл с адресами электронной почты
    receivers = f.read().splitlines()

for receiver in receivers:
    try:
        # Forming the email object / Формирование объекта письма
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        with open('mail.txt', 'r', encoding='utf-8') as mail_file:
            lines = mail_file.readlines()
            subject = lines[0].strip()  # Subject of the email from first line / Тема письма из первой строки
            body = ''.join(lines[1:]).strip()  # Body of the email from the second line to end of the file / Тело письма от первой строки до конца файла
        message['Subject'] = subject

        # Adding the email text / Добавление текста письма
        message.attach(MIMEText(body, 'plain'))

        # Establishing a connection with the SMTP server / Установление соединения с SMTP-сервером
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enabling TLS encryption / Включение шифрования TLS
        server.login(smtp_username, smtp_password)  # Server authentication / Аутентификация на сервере

        # Sending the email / Отправка письма
        server.sendmail(sender, receiver, message.as_string())
        print(f'Successfully sent the email to {receiver}!')
        
    except Exception as e:
        print(f'An error occurred while sending the email to {receiver}: {str(e)}')
        
    finally:
    # Ending the connection with the server / Завершение соединения с сервером
        server.quit()

with open('emails.txt', 'r') as f:  # File with email addresses / Файл с адресами электронной почты
    receivers = f.read().splitlines()
