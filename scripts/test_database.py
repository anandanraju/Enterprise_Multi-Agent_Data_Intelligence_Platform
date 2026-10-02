import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ANANDAN_RAJU\\SQLEXPRESS;"
    "DATABASE=EnterpriseAnalytics;"
    "Trusted_Connection=yes;"
)

connection = pyodbc.connect(connection_string)

cursor = connection.cursor()
cursor.execute("SELECT DB_NAME()")

database_name = cursor.fetchone()[0]

print("Connected database:", database_name)

cursor.close()
connection.close()