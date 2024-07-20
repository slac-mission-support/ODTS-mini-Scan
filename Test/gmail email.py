# All imports below are part of python built packages no need to install any exras

# smtplib provides functionality to send emails using SMTP.
import smtplib
# MIMEMultipart send emails with both text content and attachments.
from email.mime.multipart import MIMEMultipart
# MIMEText for creating body of the email message.
from email.mime.text import MIMEText
# MIMEApplication attaching application-specific data (like CSV files) to email messages.
from email.mime.application import MIMEApplication
import Sqlite_export_to_csv as exp
import os
import configparser

#dataframe_table = Sqlite_export_to_csv.fetch
config = configparser.ConfigParser()
config.read('config.ini')
local_path = config.get('Database','local_repo_path')
sender_email = config.get('General','sender_email')
os.chdir(local_path)
data = exp.sqlite_export

df = data.exported_data()
df_html = df.to_html(index=False, col_space='150px', justify='center', bold_rows=True, border=1)
dfPart = MIMEText(df_html, 'html')

Last_Name = "Ford"
First_Name = "Ryan"
Dosi_Number = "123456J"
Return_Date = '7-10-24'
emp_email = 'email1'
sup_email = 'email2'
def_email = sender_email

#email address selection
#def email_selection():
#   if emp_email is None:
#       recipient_email == sup_email
#       return("sup_email")
#   elif sup_email is None:
#       recipient email == def_email
#       return("def_email")
#   else:
#       recipient email == emp_email
#       return("emp_email")

email_header_0 = ("This email was sent to a supervisor because the employee does not have an email on file.\n\n")
email_header_1 = ("This email was sent to RP because there are no email addresses on file for this individual.\n\n")

email_header_2 = ("Dear " + First_Name + ",\n\n"
                "Thank you for returning your dosimeter #" + Dosi_Number + ".  "
                "We scanned it into our system on " + Return_Date + ".  "
                "If you are on a quarterly exchange, please remember to return "
                "your next dosimeter within 2 weeks of the due date. \n\n\n")

email_footer = ("\n\n\nIf you have any questions regarding the dosimetery service, "
                "please contact ESH-DREP@SLAC.STANFORD.EDU. \n\n\n")

smtp_username = config.get('General','smtp_username')
smpt_password = config.get('General','smtp_password')
smtp_host = config.get('General','smtp_host')
smtp_port = int(config.get('General','smtp_port'))

subject = "Email Subject"
body0 = email_header_0
body = email_header_2
body2 = email_footer
#sender_email = sender_email #will be esh-drep
sender_email = smtp_username
recipient_email = "three25seventy@gmail.com"
path_to_file = 'ryan1.txt'

# MIMEMultipart() creates a container for an email message that can hold
# different parts, like text and attachments and in next line we are
# attaching different parts to email container like subject and others.

#email message selection
#def email_body():
#   email = email_selection()
#   if email == sup_email:
#       send email 1 with email_header_0 and email_header_2
#   elif email == def_email:
#       send email 2 with email_header_1 and email_header_2
#   else:
#       send email 3 with email_header_2 only

message = MIMEMultipart()
message['Subject'] = subject
message['From'] = sender_email
message['To'] = recipient_email
body_part0 = MIMEText(body0)
body_part = MIMEText(body)
body_part2 = MIMEText(body2)
message.attach(body_part0)
message.attach(body_part)
message.attach(dfPart)
message.attach(body_part2)

# section 1 to attach file
with open(path_to_file,'rb') as file:
    # Attach the file with filename to the email
    message.attach(MIMEApplication(file.read(), Name="ryan1.txt"))

# secction 2 for sending email

with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
   server.login(smtp_username, smtp_password)
   server.sendmail(sender_email, recipient_email, message.as_string())
