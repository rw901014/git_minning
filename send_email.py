import smtplib
import gamification

test_score,fun_score,gamification = gamification.gamification()

gmail_user = 'rwlovezy@gmail.com'
gmail_password = 'rw885714'

sent_from = gmail_user
to = ['renw@tcd.ie']
subject = 'Gamification Score'
body = 'Hi,\n this is your gamification score: '\
    +str(gamification[0])+'\nyour engagement score on testing code is :'\
    +str(test_score[0])+'\nyour engagement score on functional code is :' \
    +str(fun_score[0])+'\nif you have any questions, please contact with me. \n Thank you'



email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ",".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
