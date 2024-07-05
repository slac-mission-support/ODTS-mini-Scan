import email_class

email = email_class.email()


slac_ID = 'A1234545'
name = 'Ryan Ford'
email_address = 'three25seventy@gmail.com'
return_date = '11/30/2023'
period_code = 'Q42023'
dosimeter_number = 'A2321ZYF'
supervisor_email = 'ryanford@slac.stanford.edu'
recipients = [email_address, supervisor_email]
#select body_option 1 for no outstanding returns
#select body_option 2 for 1 or more outstanding dosimeter returns, and provide a table.
#print(recipients)

email.send_email(slac_ID, name, recipients, return_date, period_code, dosimeter_number, 2)
