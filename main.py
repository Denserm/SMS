import smtplib
from email.message import EmailMessage
from tkinter import *


def save():
    with open('save.txt', 'w', encoding='utf-8') as file:
        file.write(f"{sender_email_entry.get()}\n")
        file.write(f"{recipient_email_entry.get()}\n")
        file.write(f"{password_entry.get()}\n")


def send_email():
    save()
    sender_email = sender_email_entry.get()
    recipient_mail = recipient_email_entry.get()
    password = password_entry.get()
    subject = subject_entry.get()
    body = body_text.get(1.0, END)

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_mail

    server = None

    try:
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.login(sender_email, password)
        server.send_message(msg)
        result_label.config(text='Письмо отправлено!')
    except Exception as e:
        result_label.config(text=f'Ошибка: {e}')
    finally:
        if server:
            server.quit()

window = Tk()
window.title('Отправка Email')
window.geometry('500x300')

Label(window, text="Отправитель:").grid(row=0, column=0, sticky=W)
sender_email_entry = Entry(window)
sender_email_entry.grid(row=0, column=1, sticky=W)

Label(window, text="Получатель:").grid(row=1, column=0, sticky=W)
recipient_email_entry = Entry(window)
recipient_email_entry.grid(row=1, column=1, sticky=W)

Label(window, text="Пароль приложения:").grid(row=2, column=0, sticky=W)
password_entry = Entry(window)
password_entry.grid(row=2, column=1, sticky=W)

Label(window, text="Тема письма:").grid(row=3, column=0, sticky=W)
subject_entry = Entry(window)
subject_entry.grid(row=3, column=1, sticky=W)

Label(window, text="Сообщение:").grid(row=4, column=0, sticky=W)
body_text = Text(window, width=45, height=10)
body_text.grid(row=4, column=1, sticky=W)

Button(window, text='Отправить письмо', command=send_email).grid(row=5, column=1, sticky=W)

result_label = Label(text='')
result_label.grid(row=6, column=1, sticky=W)

window.mainloop()