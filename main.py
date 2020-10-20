import os
import smtplib

SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
SENDER_PASS = os.environ.get('SENDER_PASS')
RECIEVER_EMAIL = os.environ.get('RECIEVER_EMAIL')

with smtplib.SMTP('localhost', 1025) as smtp:
    subject = 'TEST SUBJECT'
    body = 'TEST BODY'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(SENDER_EMAIL, RECIEVER_EMAIL, msg)




# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login(SENDER_EMAIL, SENDER_PASS)

#     subject = 'TEST SUBJECT'
#     body = 'TEST BODY'

#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(SENDER_EMAIL, RECIEVER_EMAIL, msg)