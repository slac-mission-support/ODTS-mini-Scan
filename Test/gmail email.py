# All imports below are part of python built packages no need to install any exras

# smtplib provides functionality to send emails using SMTP.
import smtplib
# MIMEMultipart send emails with both text content and attachments.
from email.mime.multipart import MIMEMultipart
# MIMEText for creating body of the email message.
from email.mime.text import MIMEText
# MIMEApplication attaching application-specific data (like CSV files) to email messages.
from email.mime.application import MIMEApplication
import os
import configparser
import Oracle_dataframe as dataframe
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')
local_path = config.get('Database','local_repo_path')
sender_email = config.get('General','sender_email')
slac_id = config.get('General', 'slac_ID')
os.chdir(local_path)
data_unreturned = dataframe.return_dataframe_view1()

df2 = data_unreturned.return_dataframe(str(slac_id))
df2_string = df2.to_string(index=False)
#print(df2_string)
df2.style.hide(axis='index')
df2_html = df2.to_html(index=False, col_space='150px', justify='center', bold_rows=True, border=1)
dfPart2 = MIMEText(df2_html, 'html')


#['Dosi#', 'Quarter', 'SLAC ID', 'Name', 'email', 'Sup SLAC ID', 'Sup Name', 'Sup email', 'return date']
Full_Name = df2.get('Name')
Full_Name_Styled = Full_Name.to_string(index=False)
print("Full Name: " + Full_Name_Styled)
First_Name = 'Ryan'
First_Name = Full_Name_Styled.split(", ")[1]
print("First Name: " + First_Name)
Last_Name = Full_Name_Styled.split(",")[0]
print("Last Name: " + Last_Name)
Dosi_Number = df2.get('Dosi#')
Dosi_Number_Styled = Dosi_Number.to_string(index=False)
print("Dosi Number: " + Dosi_Number_Styled)
Return_Date = df2.get('return date')
Return_Date_Styled = Return_Date.to_string(index=False)
print("Return Date: " + Return_Date_Styled)
emp_email = df2.get('email')
emp_email_styled = emp_email.to_string(index=False)
print("Email: " + emp_email_styled)
sup_email = df2.get('Sup email')
sup_email_styled = sup_email.to_string(index=False)
print('Sup Email: ' + sup_email_styled)
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

email_header_0 = ("This email was sent to a supervisor because the employee does not have an email on file.\n")
email_header_1 = ("This email was sent to RP because there are no email addresses on file for this individual.\n")

email_header_2 = ("Dear " + First_Name + ",\n\n"
                "Thank you for returning your dosimeter #" + Dosi_Number_Styled + ".  "
                "We scanned it into our system on " + Return_Date_Styled + ".  "
                "If you are on a quarterly exchange, please remember to return "
                "your next dosimeter within 2 weeks of the due date. \n\n\n")

email_footer = ("\n\n\nIf you have any questions regarding the dosimetery service, "
                "please contact ESH-DREP@SLAC.STANFORD.EDU. \n\n\n")

smtp_username = config.get('General','smtp_username')
smtp_password = config.get('General','smtp_password')
smtp_host = config.get('General','smtp_host')
smtp_port = int(config.get('General','smtp_port'))

subject = "Email Subject"
sender_email = smtp_username
recipient_email = "ryanford@slac.stanford.edu"
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
message.attach(MIMEText(email_header_0))
message.attach(MIMEText(email_header_2))
message.attach(dfPart2)
message.attach(MIMEText(email_footer))

print("Sender Email: " + sender_email) 
print('\n')
print('Recipient Email: ' + recipient_email)
print('\n')
print(email_header_0)
print(email_header_1)
print(email_header_2)
print(df2)
print(email_footer)


#print(smtp_host)
#print(smtp_port)

# section 1 to attach file
with open(path_to_file,'rb') as file:
    # Attach the file with filename to the email
    message.attach(MIMEApplication(file.read(), Name="ryan1.txt"))

# secction 2 for sending email

#print(message.as_string())

# try:
        
        # with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
           # server.login(smtp_username, smtp_password)
           # server.sendmail(sender_email, recipient_email, message.as_string())

# except Exception as e:
        # print(e)
        # print(type(e))


# try:
        
        # with smtplib.SMTP(smtp_host, smtp_port, timeout = 5) as server:
           # #server.login(smtp_username, smtp_password)
           
           # server.sendmail(sender_email, recipient_email, message.as_string())
           # server.quit()

# except Exception as e:
        # print(e)
        # print(type(e))
