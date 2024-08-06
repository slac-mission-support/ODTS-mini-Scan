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


def send_email():
        

        config = configparser.ConfigParser()
        config.read('config.ini')
        local_path = config.get('Database','local_repo_path')
        sender_email = config.get('General','sender_email')
        slac_id = config.get('General', 'slac_ID')
        First_Name = config.get('General', 'first_name')
        Dosi_Number = '***' + config.get('General', 'dosi_number')[-4:]
        todays_date = config.get('General','todays_date')
        Return_Date = config.get('General', 'return_date')
        email = config.get('General','email')
        sup_email = config.get('General','sup_email')
        sender_email = config.get('General','return_to_email')
        if not email:   
                email_origin = email.split('@')[1]
        else:
                email_origin = ''
        Return_Date_Year = todays_date[0:4]
        Return_Date_Month = todays_date[5:7]
        Return_Date_Day = todays_date[8:10]
        Return_Date_calculated = Return_Date_Month + "/" + Return_Date_Day + "/" + Return_Date_Year

        os.chdir(local_path)
        data_unreturned = dataframe.return_dataframe_view1()
        df2 = data_unreturned.return_dataframe(str(slac_id))

        if df2 is None:
                dfPart2 = None
                text = ''
        else:
                text = ('Our records indicate you have additional unreturned dosimeter(s).  '
                        'This could be from a prior quarter, or having replaced a dosimeter left at home. \n')
                df2_html = df2.to_html(index=False, col_space='150px', justify='center', bold_rows=True, border=1)
                dfPart2 = MIMEText(df2_html, 'html')

        #email address selection
        if email is None or email_origin != 'slac.stanford.edu':
                if sup_email is None:
                        recipient_email = sender_email
                        email_header_0 = ("This email was sent to RP because there are no email addresses on file for this individual.\n")
                else:
                        recipient_email = sup_email
                        email_header_0 = ("This email was sent to a supervisor because the employee does not have an email on file.\n")

        elif email_origin == 'slac.stanford.edu':
                recipient_email = email
                email_header_0 = ''
        else:
                recipient_email = sender_email
                email_header_0 = ("This email was sent to RP because there are no email addresses on file for this individual.\n")

        email_header_2 = ("Dear " + First_Name + ",\n\n"
                        "Thank you for returning your dosimeter #" + Dosi_Number + ".  "
                        "We scanned it into our system on " + Return_Date_calculated + ".  "
                        "If you are on a quarterly exchange, please remember to return "
                        "your next dosimeter within 2 weeks of the due date. \n")
                        
        email_header_3 = text
        
        email_footer = ("\nIf you have any questions regarding the dosimetery service, "
                        "please contact ESH-DREP@SLAC.STANFORD.EDU. \n\n"
                        "Sincerely, \n\nRadiation Protection Dosimetry Group\n\n")

        smtp_username = config.get('General','smtp_username')
        smtp_password = config.get('General','smtp_password')
        smtp_host = config.get('General','smtp_host')
        smtp_port = int(config.get('General','smtp_port'))

        subject = "Secure:  Dosimeter Return Acknowledgment"
        sender_email = smtp_username
        path_to_file = 'ryan1.txt'

        # MIMEMultipart() creates a container for an email message that can hold
        # different parts, like text and attachments and in next line we are
        # attaching different parts to email container like subject and others.

        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = recipient_email
        message.attach(MIMEText(email_header_0))
        message.attach(MIMEText(email_header_2))
        message.attach(MIMEText(email_header_3))
        message.attach(dfPart2)
        message.attach(MIMEText(email_footer))

        print("Sender Email: " + sender_email) 
        print('Recipient Email: ' + recipient_email)
        print('\n')
        print(email_header_0)
        print(email_header_2)
        print(email_header_3)

        if df2 is not None:
                print(df2.to_string(index=False))

        print(email_footer)

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

send_email()
