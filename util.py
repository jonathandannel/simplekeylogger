import subprocess
import smtplib

def send_mail(email, password, message):
	print('BEGIN LOG MESSAGE___')
	print(message)
	print('___END')
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit

