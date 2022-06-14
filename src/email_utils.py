import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = "info@smartvidboost.com"
password = "admin@SVBoost"
mail_from = "info@smartvidboost.com"
mail_to = "sandy.tnhlabs@gmail.com"
mail_subject = "Test Subject"
mail_body = "This is a test message"

mimemsg = MIMEMultipart()
mimemsg['From'] = mail_from
mimemsg['To'] = mail_to
mimemsg['Subject'] = mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.office365.com', port=587)
connection.starttls()
connection.login(username, password)
connection.send_message(mimemsg)
connection.quit()
