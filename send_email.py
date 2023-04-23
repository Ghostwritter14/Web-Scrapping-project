import smtplib
import ssl


def send_email(subject, message):
    host = "smtp.gmail.com"
    port = 465

    username = "sohamtestport@gmail.com"
    password = "kmouxhqllagadsqi"

    sender = "sohamtestport@gmail.com"
    receiver = "sohamtestport@gmail.com"
    headers = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(sender, receiver, headers + message)

    print("Email was sent")

