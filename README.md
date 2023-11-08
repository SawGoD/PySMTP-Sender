# PySMTP-Sender

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Montserrat&weight=500&size=25&duration=2800&pause=800&color=DC143C&vCenter=true&width=500&height=30&lines=S+U+T+I+V+I+S+M+Project.;.)

[![Telegram](https://img.shields.io/badge/SawGoD-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/SawGoD)

---

### О проекте:
Главная цель этого проекта - осуществлять массовую рассылку писем через SMTP сервер. 

Для этого используется код, представленный в файле `main.py`. В этом файле реализована логика формирования и отправки писем с помощью библиотеки `smtplib`. Для работы с SMTP сервером используются параметры, которые хранятся в файле `.env`. В файле `emails.txt` содержатся адреса электронной почты получателей, а в файле `mail.txt` содержится текст письма, включая тему и тело письма. 

При отправке писем происходит обработка возможных ошибок и вывод соответствующих сообщений в консоль.

---

### Основные параметры .env:
`SENDER=sender@domain` - Электронная почта отправителя

`SMTP_SERVER=smtp.server.ru` - SMTP сервер

`SMTP_USERNAME=username` - Имя пользователя SMTP сервера

`SMTP_PASSWORD=password` - Пароль SMTP сервера

### Вид файла mail.txt:
`Subject` - Тема письма, берётся из первой строки.

`Body` - Тело письма, начинается с первой строки и до конца файла.
<details>
    <summary>Раскрыть</summary>

```txt
Subject
Body
body
body
```
</details>

### Вид файла email.txt:
<details>
    <summary>Раскрыть</summary>

```txt
receiver0@domain
receiver1@domain
receiver2@domain
```
</details>
