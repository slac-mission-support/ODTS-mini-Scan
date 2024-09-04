# All imports below are part of python built packages no need to install any exras
# Test git pull 2024-08-29
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

def evaluate_email():
        config = configparser.ConfigParser()
        file_name = os.path.dirname(__file__) + '/config.ini'
        config.read(file_name)
        email_address = config.get('General','email')
        if not email_address or email_address == 'None':
                return("None", "None")
        else:
                domain = email_address.split('@')[1]
                email = email_address
                return(email_address.lower(), domain.lower())
 
evaluate_email()

def evaluate_sup_email():
        config = configparser.ConfigParser()
        file_name = os.path.dirname(__file__) + '/config.ini'
        config.read(file_name)
        email_address = config.get('General','sup_email')
        if not email_address or email_address == 'None':
                return("None", "None")
        else:
                domain = email_address.split('@')[1]
                email = email_address
                return(email_address.lower(), domain.lower())

evaluate_sup_email()


def send_email():
        

        config = configparser.ConfigParser()
        file_name = os.path.dirname(__file__) + '/config.ini'
        config.read(file_name)
        local_path = config.get('Database','local_repo_path')
        sender_email = config.get('SMTP','sender_email')
        slac_id = config.get('General', 'slac_ID')
        line_break = '<p>&#x000D;</p>'
        First_Name = config.get('General', 'first_name')
        Last_Name = config.get('General', 'last_name')
        Dosi_Number = '***' + config.get('General', 'dosi_number')[-4:]
        todays_date = config.get('General','todays_date')
        Return_Date = config.get('General', 'return_date')
        
        email = evaluate_email()[0]
        email_domain = evaluate_email()[1]
        #print(email)
        #print(email_domain)
        sup_email = evaluate_sup_email()[0]
        sup_email_domain = evaluate_sup_email()[1]
        #print(sup_email)
        
        Return_Date_Year = todays_date[0:4]
        Return_Date_Month = todays_date[5:7]
        Return_Date_Day = todays_date[8:10]
        Return_Date_calculated = Return_Date_Month + "/" + Return_Date_Day + "/" + Return_Date_Year

        os.chdir(local_path)
        data_unreturned = dataframe.return_dataframe_view1()
        df2 = data_unreturned.return_dataframe(str(slac_id))
        
        if df2 is None:
                #print("A")
                dfPart2 = ''
                df2_html = ''
                text = ''
        else:
                #print("B")
                text = ('Our records indicate you have additional unreturned dosimeter(s).  '
                        'This could be from a prior quarter, or having replaced a dosimeter left at home. \n')
                df2_html = df2.to_html(index=False, col_space='150px', justify='center', bold_rows=True, border=1)
                dfPart2 = MIMEText(df2_html, 'html')

        #email address selection
        if email == 'None' or email_domain != 'slac.stanford.edu':
                if sup_email == 'None' or sup_email_domain != 'slac.stanford.edu':
                        #print("C")
                        recipient_email = sender_email
                        email_header_0 = ("This email was sent to RP because there are no email addresses on file for this individual "
                        "or their supervisor.\n")
                else:
                        #print("D")
                        recipient_email = sup_email
                        email_header_0 = ("This email was sent to a supervisor (" + sup_email + ")"
                                        " because the employee does not have an email on file,"
                                        " or the email on file is not a SLAC email address.\n")

        else: #normal condition, i.e., email_domain == 'slac.stanford.edu':
                #print("E")
                recipient_email = email
                email_header_0 = ''

        email_header_2 = ("Dear " + First_Name + ',' + line_break +
                        "Thank you for returning your dosimeter #" + Dosi_Number + ".  "
                        "We scanned it into our system on " + Return_Date_calculated + ".  "
                        "If you are on a quarterly exchange, please remember to return "
                        "your next dosimeter within 2 weeks of the due date. \n")
                        
        email_header_3 = text
        
        email_footer = ("\nIf you have any questions regarding the dosimetery service, "
                        "please contact ESH-DREP@SLAC.STANFORD.EDU. " + line_break +
                        "Sincerely," + line_break + "Radiation Protection Dosimetry Group" + line_break +
                        "//" + slac_id + "//" + First_Name + " " + Last_Name + "//" + "RF")

        smtp_host = config.get('SMTP','smtp_host')
        smtp_port = int(config.get('SMTP','smtp_port'))

        subject = ("Secure: Dosimeter Return Acknowledgment for " + First_Name + " " + Last_Name)

        # MIMEMultipart() creates a container for an email message that can hold
        # different parts, like text and attachments and in next line we are
        # attaching different parts to email container like subject and others.

        message = MIMEMultipart('alternative')
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = 'rp-dosi@slac.stanford.edu' #recipient_email

        message.attach(MIMEText(email_header_0 + line_break + email_header_2 + line_break + email_header_3 + line_break + df2_html + line_break + email_footer, 'html'))

        try:
                
                with smtplib.SMTP(smtp_host, smtp_port, timeout = 5) as server:
                   server.sendmail(sender_email, 'rp-dosi@slac.stanford.edu', message.as_string())
                   server.quit()

        except Exception as e:
                #print(e)
                #print(type(e))
                return

#send_email()
