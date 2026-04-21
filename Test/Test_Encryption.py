import oracledb
import os

# 1. Initialize Thick mode (required for Native Network Encryption)
# Provide path to your Oracle Instant Client if not in system path
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_8")

# 2. Define connection details
# config_dir must contain your sqlnet.ora with encryption settings
config_path = "/opt/oracle/config" 
user = "hr"
password = "your_password"
dsn = "orclpdb" # Service name from tnsnames.ora

try:
    # 3. Connect using the configuration directory
    connection = oracledb.connect(
        user=user,
        password=password,
        dsn=dsn,
        config_dir=config_path
    )
    
    # 4. Verify encryption status
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT network_service_banner 
            FROM v$session_connect_info 
            WHERE sid = (SELECT sys_context('USERENV', 'SID') FROM dual)
        """)
        for row in cursor:
            print(f"Connection Info: {row[0]}") # Should mention AES256 or similar

finally:
    if 'connection' in locals():
        connection.close()
