import pandas as pd
import pyodbc
import mysql.connector
# Import CSV
data = pd.read_csv("C:/Users/amans/Downloads/mailingList.csv")
df = pd.DataFrame(data)

# Connect to SQL Server
cnxn = pyodbc.connect(driver='{SQL Server}', host="localhost", database="node-reference",
                      trusted_connection="yes", user="root", password="Aman0712")
cursor = conn.cursor()

# Create Table
cursor.execute(
    """
		CREATE TABLE mails (
			idmail int primary key,
			name nvarchar(50),
			email nvarchar(100),
			)
               """
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        """
                INSERT INTO mails (idmail, name, email)
                VALUES (?,?,?)
                """,
        row.idmail,
        row.name,
        row.email,
    )
conn.commit()
