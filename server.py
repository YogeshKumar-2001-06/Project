import pyodbc

server = 'YOGESHKUMAR\\SQLEXPRESS'
database = 'Billing_Software_project'
conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_connection=yes')
cursor = conn.cursor()