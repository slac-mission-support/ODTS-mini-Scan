
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class email():
	
	def send_email(self, slac_ID, name, recipients, return_date, period_code, dosimeter_number, body_option):
		
		#Your SMTP server
		host = "smtp.gmail.com"
		port = 465

		#Your credentials
		login = "three25seventy@gmail.com"
		password = "vweq cjhp dbfr saxk"

		#Build your email
		context = ssl.create_default_context()
		subject = "SLAC Dosimeter Return Confirmation"
		body = f"Thank you, {name}, for returning {period_code} dosimeter #{dosimeter_number} on {return_date}"
		msg = MIMEMultipart('alternative')
		msg['Subject'] = subject
		msg['From'] = login
		msg['To'] = ', '.join(recipients)
		
		if body_option == 1:
			
			text = f"Thank you, {name}, for returning {period_code} dosimeter #{dosimeter_number} on {return_date}"
		
		if body_option == 2:
		
			text = f"Thank you, {name}, for returning {period_code} dosimeter #{dosimeter_number} on {return_date}.  You still have the following dosimeters outstanding:"
		
		part1 = MIMEText(text, 'plain')
		msg.attach(part1)
		
		with smtplib.SMTP_SSL(host, port, context=context) as server:
				server.login(login, password)
				server.sendmail(login, recipients, msg.as_string())




