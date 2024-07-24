import os
import configparser



config = configparser.ConfigParser()	

class network_ping:

	def check_ping():
			config.read('config.ini')
			odts_dsn = config.get('Database','odts_server')
			hostname = odts_dsn
			response = os.system("ping -c 1 " + hostname)
			
			if response == 0:
				pingstatus = "Network Active"
			else:
				pingstatus = "Network Error"
				
			return pingstatus
			
			
	#ping_status = check_ping()
	#print(ping_status)

