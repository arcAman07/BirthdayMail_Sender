import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv("C:/Users/amans/Downloads/mailingList.csv")
df = pd.DataFrame(data)

# Connect to SQL Server
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=localhost:3306;"
    "Database=node-reference;"
    "Trusted_Connection=yes;"
)
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
