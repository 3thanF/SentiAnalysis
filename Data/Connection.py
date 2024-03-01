import pyodbc

connectionString = ( # String of values for the database connection
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=localhost;"
    "Database=PROYECTO;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

connection = pyodbc.connect(connectionString)

cursor = connection.cursor()

cursor.execute("SELECT * FROM googleplaystore")

for row in cursor:
    print(row)