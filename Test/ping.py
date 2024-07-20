import os

class network_ping:
	
	def check_ping():
			hostname = "epndev.slac.stanford.edu"
			response = os.system("ping -c 1 " + hostname)
			
			if response == 0:
				pingstatus = "Network Active"
			else:
				pingstatus = "Network Error"
				
			return pingstatus
			
			
	#ping_status = check_ping()
	#print(ping_status)

