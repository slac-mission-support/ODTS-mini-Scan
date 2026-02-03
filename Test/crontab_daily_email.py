#! /usr/bin/python3
# All imports below are part of python built packages no need to install any exras

# smtplib provides functionality to send emails using SMTP.
import smtplib
# MIMEMultipart send emails with both text content and attachments.
from email.mime.multipart import MIMEMultipart
# MIMEText for creating body of the email message.
from email.mime.text import MIMEText
# MIMEApplication attaching application-specific data (like CSV files) to email messages.
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

import os
import configparser
import Sqlite_export_to_csv as dataframe
import pandas as pd
import os


def send_email():
        
        history = dataframe.sqlite_export
        
        config = configparser.ConfigParser()
        file_name = os.path.dirname(__file__) + '/config.ini'
        config.read(file_name)
        sender_email = config.get('SMTP','sender_email')
        host_name = config.get('Device_Info','hostname')
        location = config.get('Device_Info','location')
        todays_date = config.get('General','todays_date')
        days_history = config.get('General','days_history')
        line_break = '<p>&#x000D;</p>'
        df = history.exported_data()
        df.to_excel('history.xlsx')

        if df is None:
                dfPart2 = None
                text = ''
        else:
                text = ('The following table shows a history of the past 5 days on the Subject scanner:\n')
                df_html = df.to_html(index=False, col_space='150px', justify='center', bold_rows=True, border=1)
                
                
                
        email_header_0 = ("Please treat this data as PII and do not forward.\n")

        email_footer = ("\nIf you have any questions regarding the dosimetery service, "
                        "please contact ESH-DREP@SLAC.STANFORD.EDU." + line_break +
                        "Sincerely," + line_break + "Radiation Protection Dosimetry Group" + line_break)

        smtp_host = config.get('SMTP','smtp_host')
        smtp_port = int(config.get('SMTP','smtp_port'))

        subject = "Secure: " + host_name + " - " + location + ", " + days_history + "-day history."
        path_to_file = 'history.xlsx'

        # MIMEMultipart() creates a container for an email message that can hold
        # different parts, like text and attachments and in next line we are
        # attaching different parts to email container like subject and others.

        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = 'rp-dosi@slac.stanford.edu'
        message.attach(MIMEText(email_header_0 + line_break + df_html + line_break + email_footer, 'html'))
        



        #with open(path_to_file,'rb') as file:
                
        #        message.attach(MIMEApplication(file.read(), Name="history.xlsx"))
        try:
                with smtplib.SMTP(smtp_host, smtp_port, timeout = 5) as server:
                   server.sendmail(sender_email, 'rp-dosi@slac.stanford.edu', message.as_string())
                   server.quit()

        except Exception as e:
                print(e)
                print(type(e))

#if __name__ == '__send_email__':
#send_email()
