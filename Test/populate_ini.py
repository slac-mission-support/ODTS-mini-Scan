import capture_barcode

#[0] = full name
	#[1] = return date
	#[2] = slac ID
	#[3] = email
	#[4] = supervisor email
	#[5] = dosimeter number
barcode = read_barcode()
user = mydata3.return_info_view3(barcode)
global return_date
return_date = str(user[1])
global slac_id
slac_id = user[2]
global person_name
person_name = user[0]
if str(user) == 'None':
	mymessage.message7()
	sleep(int(sleep_interval))
else:
	firstname = user[0].split(", ")[1]
	lastname = user[0].split(",")[0]
	mymessage.message6a(firstname, lastname)
sleep(sleep_interval)
global email_address
email_address = user[3]
global sup_email
sup_email = user[4]
global dosi_number
dosi_number = user[5]
#populate the ini file so it's available for the email class
config.set('General','slac_ID',str(slac_id))
config.set('General','return_date', str(return_date))
config.set('General','last_name',str(lastname))
config.set('General','first_name',str(firstname))
config.set('General','email', str(email_address))
config.set('General','sup_email', str(sup_email))
config.set('General','dosi_number', str(dosi_number))
config.set('General','todays_date', str(new_return_date)[0:10])
with open('config.ini', 'w') as f:
	config.write(f)
