import oracledb
import pandas as pd
import xlsxwriter

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
				querystring0 = "select * from RAD_PROTECT_ADMIN.VW_LCWREPORT"
				querystring1 = ("SELECT SECAREA_DISPLAY, SYSTEMNAME_DISPLAY,DISPLAY_ORDER, COPPER_OR_SS, NOTES, \
					SOURCE_WATER, COLLECTION_TANK, ACCELSECT_COMPCOOLED \
					FROM RAD_PROTECT_ADMIN.LCWSTAT_REPORT WHERE TABLE_NO = '2A' AND IS_ACTIVE = 'Y' AND DISPLAY_ORDER > 0 \
					ORDER BY DISPLAY_ORDER")
				querystring2 = "select * from RAD_PROTECT_ADMIN.VW_MAX_LCW"



				#params = ([1])
				query = cursor.execute(querystring1)
				df = DataFrame(query)
				#df.columns = ["R0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
				#  "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
				#  "20", "21", "22", "23", "24", "R25"]
				print(df)
				filename = "C:\\Users\\ryanford\\OneDrive - SLAC National Accelerator Laboratory\\2025\\LCW.xlsx"
				with pd.ExcelWriter(filename) as writer:
					df.to_excel(writer, sheet_name='LCW Status Sheet')


		else:
			print("Unusable Connection.  Please check the database and network settings.")
			return
		cursor.close()
		connection.close()

return_LCW.return_info()