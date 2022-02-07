import pandas as pd
import pyodbc
import mysql.connector
from mysql.connector import errorcode
# Import CSV
data = pd.read_csv("C:/Users/amans/Downloads/mailingList.csv")
df = pd.DataFrame(data)
# Connect to SQL Server
try:
  conn = mysql.connector.connect(user='root',
                                database='node-reference')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

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
