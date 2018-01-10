import smtplib

"""
send mail
"""

def eparam(esender, epwd, ereceiver, ebody):

esender = 'monstermon1972@gmail.com'
epwd = 'Eskimo72'
ereceiver = 'ramongreyes@icloud.com'
ebody = 'Subject : Kulafu\n\nDear Pogi, \nI got you. \n\n - MonPogi'


conn = smtplib.SMTP('smtp.gmail.com',587)
type(conn)
conn
conn.ehlo()
conn.starttls()
conn.login(esender, epwd)
conn.sendmail(esender, ereceiver, ebody)
{}
conn.quit()

