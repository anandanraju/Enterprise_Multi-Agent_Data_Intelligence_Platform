import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ANANDAN_RAJU\\SQLEXPRESS;"
    "Trusted_Connection=yes;"
)

connection = pyodbc.connect(connection_string)
connection.autocommit = True

cursor = connection.cursor()

cursor.execute("""
IF DB_ID('EnterpriseAnalytics') IS NULL
BEGIN
    CREATE DATABASE [EnterpriseAnalytics]
END
""")

print("EnterpriseAnalytics database is ready")

cursor.close()
connection.close()