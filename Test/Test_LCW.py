import oracledb
import pandas as pd

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

class return_LCW:

	def return_info():

		odts_username = 'LCWSTATUS'
		odts_password = 'mkVEbrfsJW2#36%T'
		odts_dsn = 'slacprod.slac.stanford.edu/slacprod'
		connection = oracledb.connect (
			user=odts_username,
			password=odts_password,
			dsn=odts_dsn)

		if connection.is_healthy():
				from pandas import DataFrame
				print("Connection is Healthy")
				cursor = connection.cursor()
				query = cursor.execute("select * from RAD_PROTECT_ADMIN.VW_LCWREPORT")
				df = DataFrame(query)
				print(df)

		else:
			print("Unusable Connection.  Please check the database and network settings.")
			return
		cursor.close()
		connection.close()

return_LCW.return_info()